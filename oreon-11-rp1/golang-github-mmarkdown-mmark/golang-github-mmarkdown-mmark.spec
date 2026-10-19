%global source0_hash 1fc9d26b4c2910e72c7ee94c80d2fb1707aaae2d278204c68557ccd1802a2c08
%bcond check 0
%global goipath         github.com/mmarkdown/mmark
Version:                2.2.10
%gometa
%global common_description %{expand:
Mmark is a powerful markdown processor written in Go, geared towards writing
IETF documents. It is, however, also suited for writing complete books and other
technical documentation, like the Learning Go book (mmark source, and I-D text
output).}
%global golicenses      LICENSE
%global godocs          FAQ.md README.md mmark.1.md Syntax.md 
Name:           %{goname}
Release:        1%{?dist}
Summary:        Powerful markdown processor in Go geared towards the IETF
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/mmark-%{version}.tar.gz
%if %{with check}
%endif
Obsoletes: golang-github-miekg-mmark < 1.3.6-3
Provides: golang-github-miekg-mmark = %{version}-%{release}
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

%gobuild -o %{gobuilddir}/bin/mmark %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
