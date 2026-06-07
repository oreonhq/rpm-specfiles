%global source0_hash 9a4032202fc0d2b0858f41b167389a9cfe52ac24ec282e6479b90765319de113

Name:           mailcap
Version:        2.1.54
Release:        10%{?dist}
Summary:        Helper application and MIME type associations for file types

License:        LicenseRef-Fedora-Public-Domain AND MIT AND metamail
URL:            https://pagure.io/mailcap
Source0:        mailcap-%{version}.tar.xz
BuildRequires: make
BuildRequires:  perl-interpreter
# the test script is written in python
BuildRequires:  python3
BuildArch:      noarch

%description
The mailcap file is used by the metamail program.  Metamail reads the
mailcap file to determine how it should display non-text or multimedia
material.  Basically, mailcap associates a particular type of file
with a particular program that a mail agent or other program can call
in order to handle the file.  Mailcap should be installed to allow
certain programs to be able to handle non-text files.

Also included in this package is the mime.types file which contains a
list of MIME types and their filename "extension" associations, used
by several applications e.g. to determine MIME types for filenames.

%package     -n nginx-mimetypes
Summary:        MIME type mappings for nginx
License:        LicenseRef-Fedora-Public-Domain
Requires:       nginx-filesystem

%description -n nginx-mimetypes
MIME type mappings for nginx.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q


%build
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install sysconfdir=%{_sysconfdir} mandir=%{_mandir}


%check
make check


%files
%license COPYING
%doc NEWS
%config(noreplace) %{_sysconfdir}/mailcap
%config(noreplace) %{_sysconfdir}/mime.types
%{_mandir}/man5/mailcap.*

%files -n nginx-mimetypes
%license COPYING
%doc NEWS
%config(noreplace) %{_sysconfdir}/nginx/mime.types


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.54-10
- Prepare for Oreon 11 (RP1)
