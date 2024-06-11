import csv
from typing import List, Dict


def export_csv(
    filename: str,
    fieldnames: list,
    data: List[Dict],
) -> None:
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for row in data:
            writer.writerow(row)


def main():
    with open('vote_results.csv') as f:
        vote_results = [row for row in csv.DictReader(f)]

    with open('legislators.csv') as f:
        legislators = {
            row['id']: row['name']
            for row in csv.DictReader(f)
        }

    with open('votes.csv') as f:
        votes = {
            row['id']: {
                'bill_id': row['bill_id']
            }
            for row in csv.DictReader(f)
        }

    with open('bills.csv') as f:
        bills = {
            row['id']: {
                'title': row['title'],
                'primary_sponsor': legislators.get(row['sponsor_id'], 'Unknown')
            }
            for row in csv.DictReader(f)
        }

    # Deliverable 1 
    legislators_count = {}

    for vote_result in vote_results:
        legislator_id = vote_result['legislator_id']
        if legislator_id not in legislators_count: 
            legislators_count[legislator_id] = {
                'id': legislator_id,
                'name': legislators[legislator_id],
                'num_supported_bills': 0,
                'num_opposed_bills': 0,
            }

        if vote_result['vote_type'] == '1':
            legislators_count[legislator_id]['num_supported_bills'] += 1
        elif vote_result['vote_type'] == '2':
            legislators_count[legislator_id]['num_opposed_bills'] += 1

    export_csv('legislators-support-oppose-count.csv',
               ['id', 'name', 'num_supported_bills', 'num_opposed_bills'],
               legislators_count.values())

    # Deliverable 2
    bills_count = {}

    for vote_result in vote_results:
        vote_id = vote_result['vote_id']
        if vote_id not in bills_count:
            bill_id = votes[vote_id]['bill_id']
            bill = bills[bill_id]
            bills_count[vote_id] = {
                'id': bill_id,
                'title': bill['title'],
                'supporter_count': 0,
                'opposer_count': 0,
                'primary_sponsor': bill['primary_sponsor'],
            }

        if vote_result['vote_type'] == '1':
            bills_count[vote_id]['supporter_count'] += 1
        elif vote_result['vote_type'] == '2':
            bills_count[vote_id]['opposer_count'] += 1

    export_csv('bills-support-oppose-count.csv',
               ['id', 'title', 'supporter_count', 'opposer_count', 'primary_sponsor'],
               bills_count.values())


if __name__ == '__main__':
    main()