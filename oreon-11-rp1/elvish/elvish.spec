%global source0_hash 3a4b93c3c99fe2f9847de35d64be24e2d4b9c12d429cd9831b4571993a66bb7a
%bcond check 0
%global goipath         src.elv.sh
%global forgeurl        https://github.com/elves/elvish
Version:                0.21.0
%gometa -L -f
%global common_description %{expand:
Powerful scripting language & Versatile interactive shell.}
Name:           elvish
Release:        1%{?dist}
Summary:        Powerful scripting language & Versatile interactive shell
License:        EPL-1.0 AND BSD-2-Clause AND BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         https://github.com/elves/elvish/commit/d92693380e4998ad250700aeff8f6229cf20ab7f.patch
Provides:       golang-github-elves-elvish = %{version}-%{release}
Obsoletes:      golang-github-elves-elvish < 0.15.0-12
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

mv pkg/diff/LICENSE pkg-diff-LICENSE
mv pkg/md/spec/LICENSE pkg-md-spec-LICENSE
mv pkg/persistent/LICENSE pkg-persistent-LICENSE
mv pkg/rpc/LICENSE pkg-rpc-LICENSE
mv vscode/LICENSE vscode-LICENSE

%build

%gobuild -o %{gobuilddir}/bin/elvish %{goipath}/cmd/elvish
%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%if %{with check}
%ifarch ppc64le
%gocheck -d pkg/shell
%else
%gocheck
%oreon_autofiles main
%endif
%else
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
