%global source0_hash 3eac2cfb3b1de9d14b6a712941985d6b240b7f3726c94a5e337317c7161e869d

%bcond_with tests # disable tests by default due to missing bats-assert and bats-support

Name:           diff-so-fancy
Version:        1.4.4
Release:        %autorelease
Summary:        Good-lookin' diffs

License:        MIT
URL:            https://github.com/so-fancy/diff-so-fancy
Source0:        %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  sed

%if %{with tests}
BuildRequires:  bats
BuildRequires:  bats-assert
BuildRequires:  bats-support
BuildRequires:  git
%endif

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
# nothing to build

%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 lib/DiffHighlight.pm %{buildroot}%{_datadir}/%{name}/DiffHighlight.pm

# Fix path
sed -i 's|^use lib .*$|use lib "%{_datadir}/%{name}";|' %{buildroot}%{_bindir}/%{name}

%check
%if %{with tests}
git init
bats test
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/DiffHighlight.pm

%changelog
%autochangelog
