%global source0_hash 7f0a5133885a71b89f7a683d8f3e3616e070238424b36ae04fdbc0d7b99e3027
%ifarch aarch64 armv7hl ppc64le
%bcond_with tests
%else
%bcond_without tests
%endif
Name:           dub
Version:        1.42.0
Release:        1%{?dist}
Summary:        Package and build management system for D
License:        MIT
URL:            https://github.com/dlang/dub
Source0:        https://github.com/dlang/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  %{ldc_arches}
# oreon:deps
BuildRequires:  curl-devel
BuildRequires:  ldc
# /oreon:deps
%description
DUB is a package and build manager for D applications and libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

ldmd2 -run build.d %{_d_optflags}
./bin/dub scripts/man/gen_man.d
%install
install -Dpm0755 -t %{buildroot}%{_bindir} bin/dub
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 scripts/man/dub*.1
install -Dpm0644 scripts/bash-completion/dub.bash %{buildroot}%{_datadir}/bash-completion/completions/dub
install -Dpm0644 -t %{buildroot}%{_datadir}/fish/completions scripts/fish-completion/dub.fish
install -Dpm0644 -t %{buildroot}%{_datadir}/zsh/site-functions scripts/zsh-completion/_dub
%oreon_autofiles main
%if %{with tests}
%check

export DC=ldmd2
export DUB="%{buildroot}%{_bindir}/dub"
export PATH="%{buildroot}%{_bindir}:$PATH"
dub test
pushd test
./run-unittest.sh || true
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
