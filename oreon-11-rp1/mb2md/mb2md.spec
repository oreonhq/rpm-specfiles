%global source0_hash af45a9b5413a9fe49be0092e560485bf17efc50a4eb4a90744e380c4869f732f

Name:		mb2md
Version:	3.20
Release:	34%{?dist}
Summary:	Mailbox to maildir converter
License:	LicenseRef-Fedora-Public-Domain
URL:		http://batleth.sapienti-sat.org/projects/mb2md
Source0:	http://batleth.sapienti-sat.org/projects/mb2md/mb2md-%{version}.pl.gz
Source1:	http://batleth.sapienti-sat.org/projects/mb2md/changelog.txt
BuildArch:	noarch
BuildRequires:	perl-generators

%description
Convert your emails folders in mailbox format to maildirs.
Some of the current features of mb2md.pl are:
* converting the user's main mailbox that is referenced by the $MAIL variable
* converting a single mailbox into corresponding maildir
* converting multiple mailboxes in a directory into corresponding maildirs
* recursive operation on a given directory to convert the complete mail
  storage of one user
* replaces all occurrences of dots ('.') in a mailbox name by underscores ('_')
* is able to handle spaces in mailbox names
* converts mbox files in DOS format (CRLF) to Unix file format
* can strip an extension (e.g. ".mbx") from a mailbox name prior to converting
* removal of dummy message that a couple of IMAP servers (e.g. UW-IMAPD) put at
  the beginning of a mailbox
* setting the file date of a converted message according to the date found in
  the "From " line of the original mail
* setting the flags F,R,S,T (flagged, replied, seen, deleted) on the filename
  of the converted message according to the flags found in 
  "Status:"/"X-Status:"/"X-Mozilla-Status:"/"X-Evolution:" headers of the
  original mail

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -Tc -n %{name}-%{version}
# Setup executable
gunzip -c %{SOURCE0} > mb2md.pl
touch -r %{SOURCE0} mb2md.pl

# Copy changelog
cp -a %{SOURCE1} .

### Generate documentation
# #--- denotes the end of the documentation section; get everything before
# that, remove the shebang and the hash commentation
grep -B `wc -l mb2md.pl|awk '{print $1}'` "#---------" mb2md.pl | grep -v "#-----" | grep -v "#!/" | \
cut -c3- > readme.txt
touch -r %{SOURCE0} readme.txt

%build

%install
rm -rf %{buildroot}
install -D -p -m 755 mb2md.pl %{buildroot}%{_bindir}/mb2md

%files
%doc changelog.txt readme.txt
%{_bindir}/mb2md

%changelog
%autochangelog
