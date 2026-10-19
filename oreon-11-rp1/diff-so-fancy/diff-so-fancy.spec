%global source0_hash 6f6b6e8910821766ce55a99fd5d6c960f1943440738a36b12b66a7165188ce7d
%bcond_with tests # disable tests by default due to missing bats-assert and bats-support
Name:           diff-so-fancy
Version:        1.4.12
Release:        1%{?dist}
Summary:        Good-lookin' diffs
License:        MIT
URL:            https://github.com/so-fancy/diff-so-fancy
Source0:        https://github.com/so-fancy/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildArch:      noarch
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  bats
BuildRequires:  bats-assert
BuildRequires:  bats-support
BuildRequires:  git
BuildRequires:  perl-generators
BuildRequires:  sed
# /oreon:deps
%description
diff-so-fancy strives to make your diffs human readable instead of machine 
readable. This helps improve code quality and helps you spot defects faster.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# DiffHighlight is included
%global __requires_exclude ^perl\\((DiffHighlight)
%global __provides_exclude ^perl\\((DiffHighlight)

%if %{with tests}
# Set correct path for test dependencies
sed -e "s|load 'test_helper/bats-support.*$|bats_load_library 'bats-support'|" \
    -e "s|load 'test_helper/bats-assert.*$|bats_load_library 'bats-assert'|" \
    -i test/*.bats
%endif

%build

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 lib/DiffHighlight.pm %{buildroot}%{_datadir}/%{name}/DiffHighlight.pm
sed -i 's|^use lib .*$|use lib "%{_datadir}/%{name}";|' %{buildroot}%{_bindir}/%{name}
%oreon_autofiles main

%check

%if %{with tests}
git init
bats test
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
