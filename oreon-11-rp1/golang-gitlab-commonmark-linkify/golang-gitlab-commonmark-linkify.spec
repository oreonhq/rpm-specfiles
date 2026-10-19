%global source0_hash 6fad6a1738cd2b4e52bc24528761cadc7426f60a78bda07f93a5011b9891a03e
%bcond check 0
%global goipath         gitlab.com/golang-commonmark/linkify
%global forgeurl        https://gitlab.com/golang-commonmark/linkify
%global commit          64bca66f6ad31f726def3d4a5ebc0d947fa875d7
%gometa
%global goaltipaths     github.com/golang-commonmark/linkify
%global common_description %{expand:
Package linkify provides a way to find what looks like links in plain text.}
%global golicenses      LICENSE
%global godocs          README.md genfsm/suffixes.txt
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Find what looks like links in plain text
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{commit}/linkify-%{commit}.tar.bz2
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/text/unicode/rangetable)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in genfsm; do
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
