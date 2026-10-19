%global source0_hash 33451a782b66266c59560a5ec7f4e34c104c501a36b445fc574fad71e3b3d884
%bcond check 1
%global goipath         github.com/gopasspw/gopass
Version:                1.16.1
%gometa -L -f
%global common_description %{expand:
The slightly more awesome standard unix password manager for teams.}
Name:           gopass
Release:        1%{?dist}
Summary:        The slightly more awesome standard unix password manager for teams
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSD-3-Clause-HP AND CC0-1.0 AND ISC AND MIT AND MPL-2.0 AND (Apache-2.0 OR MIT)
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{archivename}-vendor.tar.bz2
Source2:        go-vendor-tools.toml
Requires:       git-core
Requires:       gnupg2
Recommends:     (wl-clipboard if libwayland-client else xclip)
Recommends:     (xclip if xorg-x11-server-Xorg else wl-clipboard)
# oreon:deps
BuildRequires:  git-core
BuildRequires:  gnupg2
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools
BuildRequires:  golang
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%setup -q -T -D -a1 %{forgesetupargs}

%build

export LDFLAGS="-X main.version=%{version} $(LDFLAGS)"
%gobuild -o %{gobuilddir}/bin/gopass %{goipath}
%{gobuilddir}/bin/gopass completion bash > gopass.bash
%{gobuilddir}/bin/gopass completion fish > gopass.fish
%{gobuilddir}/bin/gopass completion zsh  > gopass.zsh
%install
%go_vendor_license_install -c %{S:2}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dp gopass.bash                 %{buildroot}%{_datadir}/bash-completion/completions/gopass
install -Dp gopass.fish                 %{buildroot}%{_datadir}/fish/vendor_completions.d/gopass.fish
install -Dp gopass.zsh                  %{buildroot}%{_datadir}/zsh/site-functions/_gopass
%oreon_autofiles main

%check

%go_vendor_license_check -c %{S:2}
%if %{with check}
git config --global user.email "%{name}-owner@fedoraproject.org"
git config --global user.name "%{name} maintainer"
%gocheck -d github.com/gopasspw/gopass/internal/config -d github.com/gopasspw/gopass/internal/store/leaf -d github.com/gopasspw/gopass/internal/updater -d github.com/gopasspw/gopass/pkg/fsutil
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
