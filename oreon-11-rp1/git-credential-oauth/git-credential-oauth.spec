%global source0_hash 23769afc87f82fe21b5519d059bb5ce56b2fad2c4abc7ecde9bff49a4e065ab6
%bcond check 0
%global goipath         github.com/hickford/git-credential-oauth
Version:                0.17.2
%gometa -f
%global common_description %{expand:
A Git credential helper that authenticates to GitHub, GitLab, BitBucket and
other forges using OAuth. The first time you push, the helper will open a
browser window to authenticate. Subsequent pushes within the cache timeout
require no interaction.}
%global golicenses      LICENSE.txt
%global godocs          CONTRIBUTING.md README.md
Name:           git-credential-oauth
Release:        1%{?dist}
Summary:        Git credential helper for GitHub and other forges using OAuth
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Enhances: git
Recommends: xdg-utils
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

export GO_LDFLAGS="-X main.version=%{version}"
%gobuild -o %{gobuilddir}/bin/git-credential-oauth %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                     %{buildroot}%{_mandir}/man1
install -m 0644 -vp git-credential-oauth.1 -t %{buildroot}%{_mandir}/man1
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
