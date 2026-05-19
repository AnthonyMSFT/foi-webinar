# Sends the 10 FOI Exempt sample emails to a single recipient via the
# locally-installed Outlook desktop client (uses the account already
# signed-in to Outlook).
param(
  [string]$To = 'amberr@m365cpi64172488.onmicrosoft.com'
)

$emails = @(
  @{
    From    = 'P. Greaves'
    Subject = 'Information request - restructure mentions'
    Body    = @"
Hello,

Could you send me copies of every email, memo, briefing note and meeting minute produced by any team in your organisation over the past seven years that mentions the word 'restructure'? A spreadsheet would be fine.

Thanks,
P. Greaves
"@
  },
  @{
    From    = 'M. Cresswell'
    Subject = 'ANOTHER request - finance team details'
    Body    = @"
This is the 23rd time I have written this month. You people are clearly hiding something. Send me the names, salaries, home postcodes and disciplinary histories of everyone in your finance team or I will be contacting my MP again.

M. Cresswell
"@
  },
  @{
    From    = 'E. Quinn'
    Subject = 'Annual report and accounts'
    Body    = @"
Hello,

Please send me a copy of your most recent annual report and the audited accounts for the last three financial years.

Thanks,
E. Quinn
"@
  },
  @{
    From    = 'B. Thornton'
    Subject = 'Information about officer - case 2024/RB/0098'
    Body    = @"
Hello,

I'd like the full name, job title, work mobile number, line manager and start date of the officer who handled my neighbour's case (reference 2024/RB/0098), along with any complaints that have ever been made against them.

Regards,
B. Thornton
"@
  },
  @{
    From    = 'C. Whittaker'
    Subject = 'Surveillance information request'
    Body    = @"
Hello,

Please provide a map of all covert observation points and number-plate camera positions currently in use across the borough, together with the duty rota for the surveillance team for the next month.

Regards,
C. Whittaker
"@
  },
  @{
    From    = 'N. Voss'
    Subject = 'Legal correspondence - Bramwell Construction dispute'
    Body    = @"
Hello,

Please share all correspondence and written advice between your in-house lawyers and external counsel regarding the ongoing dispute with Bramwell Construction Ltd, including any draft witness statements and counsel's opinions.

Thanks,
N. Voss
"@
  },
  @{
    From    = 'H. Lindqvist'
    Subject = 'Highways maintenance tender documents'
    Body    = @"
Hello,

Please send me the unredacted bid documents, pricing breakdowns and internal scoring notes from every supplier who tendered for the highways maintenance contract awarded last autumn.

Kind regards,
H. Lindqvist
"@
  },
  @{
    From    = 'O. Penrose'
    Subject = 'Meeting transcript - September safeguarding discussion'
    Body    = @"
Hello,

A local business owner told you about safeguarding concerns at their premises in a private meeting last September. Please send me a full transcript of that meeting and the name of the person who raised the concerns.

Thanks,
O. Penrose
"@
  },
  @{
    From    = 'K. Ashworth (Local Gazette)'
    Subject = "Children's services inspection - draft report"
    Body    = @"
Hello,

I understand your independent inspection report into children's services is due to be published next month. Please send me the draft now so I can prepare my article.

Regards,
K. Ashworth (Local Gazette)
"@
  },
  @{
    From    = 'J. Tindall'
    Subject = 'Leadership team discussions on the depot closure'
    Body    = @"
Hello,

Please send me the unredacted minutes and any side notes from the senior leadership team meetings held between January and April 2026 that discussed the proposed depot closure. I'm particularly interested in any dissenting views and personal opinions individual directors expressed before the public consultation began.

Regards,
J. Tindall
"@
  }
)

$outlook = New-Object -ComObject Outlook.Application
$i = 0
foreach ($e in $emails) {
  $i++
  $mail = $outlook.CreateItem(0)  # 0 = MailItem
  $mail.To = $To
  $mail.Subject = $e.Subject
  $mail.Body = $e.Body
  try {
    $mail.Send()
    "[{0:D2}] Sent: {1}" -f $i, $e.Subject
  } catch {
    "[{0:D2}] FAILED: {1} -- {2}" -f $i, $e.Subject, $_.Exception.Message
  }
}

"Done. {0} emails dispatched to {1}." -f $emails.Count, $To
