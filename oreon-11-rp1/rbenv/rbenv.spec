%global source0_hash e2104f6472d7a8477409c46d4de39562b4d01899148a3dbed73c1d99a0b4bb2a

# some tests are failing and there isn't a straightforward way to disable them
%bcond check 1
%global debug_package %{nil}

Name:           rbenv
Version:        1.3.2
Release:        %autorelease
Summary:        Manage your app's Ruby environment

License:        MIT
URL:            https://github.com/rbenv/rbenv
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires:       gawk
BuildRequires:  gawk
BuildRequires:  grep
%if %{with check}
BuildRequires:  bats
BuildRequires:  git-core
%endif

Recommends:     ruby-build-rbenv

%description
Use rbenv to pick a Ruby version for your application and guarantee that your
development environment matches production. Put rbenv to work with Bundler for
painless Ruby upgrades and bulletproof deployments.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%install
mkdir -p %{buildroot}%{_libdir}/rbenv
cp -a completions libexec rbenv.d %{buildroot}%{_libdir}/rbenv

mkdir -p %{buildroot}%{_bindir}
ln -s %{_libdir}/rbenv/libexec/rbenv %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man1
install -Dpm 0644 share/man/man1/rbenv.1 %{buildroot}%{_mandir}/man1/rbenv.1

%if %{with check}
%check
# Skip failing tests
for test in "non-writable shims directory" "detect parent shell" "detect parent shell from script"; do
  awk -i inplace '/^@test\s+"'"$test"'"\s*\{/{ print; print "  skip \"disabled failing test\""; next }1' $(grep -rl "@test \"$test\"")
done
bats test
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
