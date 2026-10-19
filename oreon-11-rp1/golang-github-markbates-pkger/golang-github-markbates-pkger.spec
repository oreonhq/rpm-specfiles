%global source0_hash da775b5ec5675f0db75cf295ff07a4a034ba15eb5cc02d278a5767f387fb8273
%bcond check 1
%global goipath         github.com/markbates/pkger
Version:                0.17.1
%gometa
%global common_description %{expand:
Pkger is a tool for embedding static files into Go binaries. It will, hopefully,
be a replacement for github.com/gobuffalo/packr/v2.}
%global golicenses      LICENSE
%global godocs          examples README.md SHOULDERS.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Embed static files in Go binaries
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/pkger-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/gobuffalo/here)
BuildRequires:  golang(github.com/gobuffalo/packd)
BuildRequires:  golang(github.com/gobuffalo/packr/v2)
BuildRequires:  golang(github.com/stretchr/testify/require)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
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
