from odoo.tests.common import TransactionCase


class TestDevelopersManagement(TransactionCase):

    def setUp(self):
        super().setUp()
        self.Company = self.env['developers.management.company']
        self.Developer = self.env['developers.management.developer']

    def test_create_company_with_developers(self):
        # Create developers
        developer1 = self.Developer.write({'name': 'John',
                                            'type': 'backend',
                                            'phone': '123456789',
                                            'email': 'john@example.com', })
        developer2 = self.Developer.write({'name': 'Sam',
                                            'type': 'fullstack',
                                            'phone': '123123123',
                                            'email': 'sam@example.com', })

        # Create a company with linked developers
        company_vals = {
            'name': 'Test Company',
            'address': 'Test Address',
            'developer_ids': [(4, developer1.id), (4, developer2.id)]
        }
        company = self.Company.write(company_vals)

        # Check correct definition of global_identification
        self.assertEqual(developer1.global_identification, 'John-backend', )
        self.assertEqual(developer2.global_identification, 'Sam-fullstack', )
        # Check if company and developers are properly linked
        self.assertEqual(company.name, 'Test Company')
        self.assertEqual(len(company.developer_ids), 2)
        self.assertIn(developer1, company.developer_ids)
        self.assertIn(developer2, company.developer_ids)

