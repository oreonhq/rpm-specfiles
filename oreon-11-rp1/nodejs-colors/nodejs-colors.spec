%global source0_hash 7497891052d893350dc2310ccc918fcb050b243b8ce0057925d2025be76b5b9d

%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-colors
Version:        1.2.1
Release:        17%{?dist}
Summary:        Get colors in your Node.js console

License:        MIT
URL:            https://github.com/Marak/colors.js
Source0:        https://github.com/Marak/colors.js/archive/v%{version}/colors-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging
BuildRequires:  nodejs(engine)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup  -n colors.js-%{version}

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/colors
cp -pr package.json safe.js lib themes/ \
    %{buildroot}%{nodejs_sitelib}/colors
%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%__nodejs tests/basic-test.js && %__nodejs tests/safe-test.js
%endif

%files
%doc README.md ROADMAP.md examples
%license LICENSE
%{nodejs_sitelib}/colors

%changelog
%autochangelog
