%global source0_hash a1beb1ee03c7247c2f89792ac5bf91cb4e5ee9bdee839e2208ec9f3aacd738f2

Name:           svn2cl
Version:        0.14
Release:        24%{?dist}
Summary:        Create a ChangeLog from a Subversion log

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://arthurdejong.org/svn2cl/
Source0:        http://arthurdejong.org/svn2cl/%{name}-%{version}.tar.gz

BuildArch:      noarch
Requires:       libxslt
Requires:       subversion
Provides:       subversion-svn2cl = 1.7.0
Obsoletes:      subversion-svn2cl < 1.7.0

%description
svn2cl is a simple XSL transformation and shell script wrapper for
generating a classic GNU-style ChangeLog from a subversion repository
log.  It is made from several change log -like scripts using common
XSLT constructs found in different places.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i -e 's|^XSL="$dir/|XSL="%{_datadir}/svn2cl/|' svn2cl.sh

%build

%install
install -Dpm 755 svn2cl.sh $RPM_BUILD_ROOT%{_bindir}/svn2cl
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/svn2cl
install -pm 644 *.xsl $RPM_BUILD_ROOT%{_datadir}/svn2cl
install -Dpm 644 svn2cl.1 $RPM_BUILD_ROOT%{_mandir}/man1/svn2cl.1

%files
%doc ChangeLog NEWS README TODO authors.xml svn2html.css
%{_bindir}/svn2cl
%{_datadir}/svn2cl/
%{_mandir}/man1/svn2cl.1*

%changelog
%autochangelog
