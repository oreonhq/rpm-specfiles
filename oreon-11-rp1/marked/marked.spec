%global source0_hash f922aa64b2ca32fd1543d3af3b35705e4161e7f5abcd6ffbcad7b44f84fbdfd8
%{?nodejs_find_provides_and_requires}
%global enable_tests 0
Name:       marked
Version:    2.0.0
Release:        1%{?dist}
Summary:        A markdown parser for Node.js built for speed
License:    MIT
URL:        https://github.com/markedjs/%{name}
Source0:        https://github.com/markedjs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:  noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%if 0%{?enable_tests}
%endif
Requires:       nodejs-marked = %{version}-%{release}
# oreon:deps
BuildRequires:  nodejs
BuildRequires:  nodejs-packaging
BuildRequires:  npm
BuildRequires:  uglify-js
BuildRequires:  web-assets-devel
# /oreon:deps
%description
Install this for command line tool and man page.
%_description

# Note: the subpackages were the only way I could get upgrades
# from marked-0.3.2 or nodejs-marked-0.3.6 to work smoothly.

%package -n nodejs-marked
Summary:    A markdown parser for JavaScript built for speed
Requires:       js-marked = %{version}-%{release}
%description -n nodejs-marked

%package -n js-marked
Summary:    Minified markdown parser for JavaScript built for speed
Requires:   web-assets-filesystem
%description -n js-marked
Install this for the minified web assests for nodejs-marked.
%_description

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

# remove the bundled minified marked
rm -f marked.min.js
# Not sure what this is for, but rpmlint doesn't like it
rm -f docs/.eslintrc.json

%build

uglifyjs --comments '/Copyright/' lib/marked.js -o marked.min.js
%install
mkdir -p %{buildroot}%{_jsdir}/%{name}
cp -pr lib/marked.js marked.min.js %{buildroot}%{_jsdir}/%{name}
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr package.json component.json src \
    %{buildroot}%{nodejs_sitelib}/%{name}
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}/lib
ln -sf %{_jsdir}/marked/marked.js \
    %{buildroot}%{nodejs_sitelib}/marked/lib/marked.js
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}/bin
install -p -D -m0755 bin/%{name} \
    %{buildroot}%{nodejs_sitelib}/marked/bin/%{name}
sed -i -e '1,1 s:env node:node:' \
    %{buildroot}%{nodejs_sitelib}/marked/bin/%{name}
mkdir -p %{buildroot}/%{_bindir}
ln -sf %{nodejs_sitelib}/%{name}/bin/%{name} \
    %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m0644 man/%{name}.1 \
    %{buildroot}%{_mandir}/man1/%{name}.1
%nodejs_symlink_deps
%oreon_autofiles nodejs-marked usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles js-marked usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if 0%{?enable_tests}
%check

%nodejs_symlink_deps --check
npm run test
%endif
%files -f %{oreon_filedir}/main.list
%files -n nodejs-marked -f %{oreon_filedir}/nodejs-marked.list
%files -n js-marked -f %{oreon_filedir}/js-marked.list

%changelog

%autochangelog
