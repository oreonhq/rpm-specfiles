%global source0_hash 9fc5b6af42ebd6ebaef63d2a10f7514d4c3ddb7cc52747ebc96a2c5d1ee122a2

Name:           git-publish
Version:        1.8.2
Release:        5%{?dist}
Summary:        Prepare and store patch revisions as git tags
License:        MIT
URL:            https://github.com/stefanha/git-publish
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  perl-podlators
Requires:       git-core git-email

%description
git-publish handles repetitive and time-consuming details of managing patch
email submission.  It works with individual patches as well as patch series and
has support for pull request emails.

Each revision is stored as a git tag including the cover letter (if any).  This
makes it easy to refer back to previous revisions of a patch.  Numbering is
handled automatically and the To:/Cc: email addresses are remembered across
revisions to save you retyping them.

Many projects have conventions for submitting patches.  It is possible to
encode them as a .gitpublish file and hooks/ scripts.  This automatically uses
the right settings and can run a coding style checker or linting tools before
emails are sent.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Force Python 3
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_shebangs
sed -i '1c #!%{__python3}' git-publish

%build
pod2man --center "git-publish Documentation" --release "%{version}" git-publish.pod git-publish.1

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/git-publish/hooks
install -p -m 755 git-publish %{buildroot}%{_bindir}/
install -p -m 644 git-publish.1 %{buildroot}%{_mandir}/man1/
install -p -m 644 hooks/pre-publish-send-email.example %{buildroot}%{_datadir}/git-publish/hooks/

%files
%license LICENSE
%_bindir/git-publish
%_mandir/man1/git-publish.1*
%_datadir/git-publish/hooks/pre-publish-send-email.example

%changelog
%autochangelog
