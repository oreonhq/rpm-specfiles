%global source0_hash 1a033f212035f2e70897f42626bb1a229ff7d3a1a4067578a02842953ed2af18
%bcond check 1
%global goipath         jaytaylor.com/html2text
%global forgeurl        https://github.com/jaytaylor/html2text
%global commit          bc68cce691ba2dac2abfddc107f7f92d4615bd06
%gometa
%global goaltipaths     github.com/jaytaylor/html2text
%global common_description %{expand:
Golang HTML to plaintext conversion library.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Golang HTML to plaintext conversion library
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/html2text-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/olekukonko/tablewriter)
BuildRequires:  golang(github.com/ssor/bom)
BuildRequires:  golang(golang.org/x/net/html)
BuildRequires:  golang(golang.org/x/net/html/atom)
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
