%global source0_hash 79cb170e31605db50db02391e829ca5c0b424b8413d8a0fd635109237424d1f2
%bcond check 0
%global goipath         github.com/client9/plaintext
%global commit          5bf47e7c0c45b7bdff3779011b6d73ab638ec534
%gometa
%global common_description %{expand:
Extract human languages in plain UTF-8 text from computer code and markup.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Tools to extract plaintext from computer code and markup
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/plaintext-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/net/html)
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
