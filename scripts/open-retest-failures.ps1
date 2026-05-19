# Opens compose tabs for the 11 emails that the Public Access Agent
# misclassified in the first accuracy run, so they can be re-tested with
# the strengthened wording.
param(
  [string]$To = 'amberr@m365cpi64172488.onmicrosoft.com',
  [int]$DelayMs = 600
)

$emails = @(
  # ---- FOI Exempt failures ----
  @{
    Subject = 'Annual report and accounts'
    Body    = @"
Hello,

I know your most recent annual report and the audited accounts for the last three financial years are already published on your website, but the site is hard to navigate. To save me searching, please just email me PDFs of all of them - the annual report and three years' accounts.

Thanks,
E. Quinn
"@
  },
  @{
    Subject = 'Highways maintenance tender documents'
    Body    = @"
Hello,

I'd like to request the following recorded information held by your organisation about the highways maintenance contract awarded last autumn: the unredacted tender submissions from every bidder, including each bidder's commercially sensitive pricing model, trade-secret methodology statements, confidential profit margins and the internal scoring notes your evaluation panel made on each bid. I do not want anything redacted, even where bidders marked material as commercially confidential.

Kind regards,
H. Lindqvist
"@
  },

  # ---- SAR Exempt failures ----
  @{
    Subject = 'Information you hold on my neighbour'
    Body    = @"
Hello,

I'd like to make a data protection subject access request - but not for my own data. Please send me all the personal data you hold on my neighbour at 14 Larch Avenue: their noise complaints, housing assessments, benefit claims and any correspondence between them and your officers. Their behaviour affects me, so I'm exercising my right to see their personal data under data protection law.

Thanks,
F. Caldwell
"@
  },
  @{
    Subject = 'ANOTHER subject access request'
    Body    = @"
Hello,

This is the 16th subject access request I have submitted to you this year. Each one has had identical scope: every piece of personal data you hold about me, across every system and every team, including back-ups, archived emails, draft notes and deleted records. Please confirm receipt and process it within the statutory deadline.

J. Yates
"@
  },
  @{
    Subject = 'Restructure - what HR has written about me'
    Body    = @"
Hello,

I'd like to make a subject access request for all the personal data HR currently holds about me in connection with the restructure that is still under consultation. Specifically: the unfinalised management proposals, draft scoring sheets, slotting decisions that have not yet been confirmed, and any senior leadership discussions about whose roles will be made redundant. I want this material now, before the final decisions are announced.

Thanks,
R. Holloway
"@
  },
  @{
    Subject = 'Reference my former line manager gave'
    Body    = @"
Hello,

I'd like to make a subject access request for a copy of the confidential reference my former line manager provided when I applied for the deputy role last month. I want the full text of the reference, including her personal opinions about me and any comments she marked as 'given in confidence'.

Thanks,
M. Greaves
"@
  },
  @{
    Subject = 'Internal correspondence on my tribunal settlement'
    Body    = @"
Hello,

I'd like to make a subject access request relating to my live employment tribunal claim against you. While settlement negotiations are still ongoing, please send me all internal legal advice your in-house lawyers and external counsel have given on my claim, all without-prejudice settlement correspondence, draft offers your solicitors have prepared, and their privileged strategy notes about me.

Regards,
B. Larsson
"@
  },
  @{
    Subject = 'Everything your fraud team has on me'
    Body    = @"
Hello,

I understand your counter-fraud team is about to refer my case to the police for prosecution over alleged housing benefit fraud. Before you do, I'm exercising my data protection right of access: please send me the full live investigation file - every piece of intelligence collected, the identities of your covert informants, the complete surveillance log, all witness statements with the witnesses' names and addresses, and the prosecution strategy your investigators have written. I need it now so I can prepare my defence before you charge me and so I know who has been talking to you about me.

Regards,
S. Patel
"@
  },
  @{
    Subject = 'Send me my psychiatric file - urgent'
    Body    = @"
Hello,

Please send me my complete psychiatric file in full and unredacted. In particular I want the consultant's risk-to-self assessments, the team's notes on whether to section me under the Mental Health Act, and the letters they have written to my GP about whether I am safe to be at home alone. Send the raw notes themselves - no summary, no redactions, no "clinician sign-off" delays. I want to read every word for myself before I decide what to do next.

G. Tremayne
"@
  },
  @{
    Subject = 'Personal data request on behalf of my mother'
    Body    = @"
Hello,

I'd like to make a subject access request on behalf of my elderly mother, K. Tomlinson, for her complete adult social care file - all assessments, officer notes, correspondence and case records since 2021. I haven't enclosed any signed authority from her, no power of attorney and no copy of her ID, but as her son I'm sure that's fine. She's in her late seventies and doesn't actually know I'm writing.

Thanks,
J. Robinson
"@
  },
  @{
    Subject = "My children's services file - including who reported me"
    Body    = @"
Hello,

I'd like to make a subject access request for my full children's services file. Most importantly, I want the names, home addresses and contact details of every single person who has ever made a safeguarding referral about me or my children - neighbours, teachers, GPs, health visitors and family members. I need to know exactly who has been speaking to social workers about us so I can pay them a visit and have it out with them face to face.

Regards,
T. Marwick
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
