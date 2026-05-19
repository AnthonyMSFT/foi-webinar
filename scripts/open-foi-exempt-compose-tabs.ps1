# Opens 10 pre-filled OWA compose tabs in the default browser.
param(
  [string]$To = 'amberr@m365cpi64172488.onmicrosoft.com',
  [int]$DelayMs = 600
)

$emails = @(
  @{
    Subject = 'Information request - restructure mentions'
    Body    = @"
Hello,

I'd like to request the following recorded information held by your organisation: copies of every email, memo, briefing note and meeting minute produced by any team over the past seven years that mentions the word 'restructure'. A spreadsheet would be fine.

Thanks,
P. Greaves
"@
  },
  @{
    Subject = 'ANOTHER request - finance team details'
    Body    = @"
This is the 23rd time I have written this month. You people are clearly hiding something. As before, I am requesting the recorded information you hold about your finance team - specifically the names, salaries, home postcodes and disciplinary histories of every member - or I will be contacting my MP again.

M. Cresswell
"@
  },
  @{
    Subject = 'Annual report and accounts'
    Body    = @"
Hello,

I'd like to request the following recorded information held by your organisation: a copy of your most recent annual report and the audited accounts for the last three financial years.

Thanks,
E. Quinn
"@
  },
  @{
    Subject = 'Information about officer - case 2024/RB/0098'
    Body    = @"
Hello,

I'd like to request the following recorded information held by your organisation: the full name, job title, work mobile number, line manager and start date of the officer who handled my neighbour's case (reference 2024/RB/0098), along with any complaints that have ever been made against them.

Regards,
B. Thornton
"@
  },
  @{
    Subject = 'Surveillance information request'
    Body    = @"
Hello,

I'd like to request the following recorded information held by your organisation: a map of all covert observation points and number-plate camera positions currently in use across the borough, together with the duty rota for the surveillance team for the next month.

Regards,
C. Whittaker
"@
  },
  @{
    Subject = 'Legal correspondence - Bramwell Construction dispute'
    Body    = @"
Hello,

I'd like to request the following recorded information held by your organisation: all correspondence and written advice between your in-house lawyers and external counsel regarding the ongoing dispute with Bramwell Construction Ltd, including any draft witness statements and counsel's opinions.

Thanks,
N. Voss
"@
  },
  @{
    Subject = 'Highways maintenance tender documents'
    Body    = @"
Hello,

I'd like to request the following recorded information held by your organisation: the unredacted bid documents, pricing breakdowns and internal scoring notes from every supplier who tendered for the highways maintenance contract awarded last autumn.

Kind regards,
H. Lindqvist
"@
  },
  @{
    Subject = 'Meeting transcript - September safeguarding discussion'
    Body    = @"
Hello,

I'd like to request the following recorded information held by your organisation. A local business owner told you about safeguarding concerns at their premises in a private meeting last September. Please send me a full transcript of that meeting and the name of the person who raised the concerns.

Thanks,
O. Penrose
"@
  },
  @{
    Subject = "Children's services inspection - draft report"
    Body    = @"
Hello,

I'd like to request the following recorded information held by your organisation. I understand your independent inspection report into children's services is due to be published next month. Please send me the draft now so I can prepare my article.

Regards,
K. Ashworth (Local Gazette)
"@
  },
  @{
    Subject = 'Leadership team discussions on the depot closure'
    Body    = @"
Hello,

I'd like to request the following recorded information held by your organisation: the unredacted minutes and any side notes from the senior leadership team meetings held between January and April 2026 that discussed the proposed depot closure. I'm particularly interested in any dissenting views and personal opinions individual directors expressed before the public consultation began.

Regards,
J. Tindall
"@
  }
)

$i = 0
foreach ($e in $emails) {
  $i++
  $subj = [Uri]::EscapeDataString($e.Subject)
  $body = [Uri]::EscapeDataString($e.Body)
  $toEnc = [Uri]::EscapeDataString($To)
  $url  = "https://outlook.office.com/mail/deeplink/compose?to=$toEnc&subject=$subj&body=$body"
  Start-Process $url
  "[{0:D2}] Opened: {1}" -f $i, $e.Subject
  Start-Sleep -Milliseconds $DelayMs
}

"Done. Opened {0} compose tabs to {1}." -f $emails.Count, $To
