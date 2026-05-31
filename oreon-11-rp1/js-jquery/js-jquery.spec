%global source0_hash 6150ac588f06b2bbcb277bbba6d696c296f1ee88160065a84b56e93c54fd1f64
%global source1_hash 164a251e86a8e5fc76b9bf074b2d91b4a876ba10b45c45d8017b53fd96415226

Name:           js-jquery
Version:        3.7.1
Release:        8%{?dist}
Summary:        JavaScript DOM manipulation, event handling, and AJAX library
BuildArch:      noarch

%global ver_x %(echo %{version} | cut -d. -f1)
%global ver_y %(echo %{version} | cut -d. -f2)
%global ver_z %(echo %{version} | cut -d. -f3)

License:        MIT
URL:            https://jquery.com/
Source0:        https://github.com/jquery/jquery/archive/%{version}/jquery-%{version}.tar.gz
# Created by ./update-sources.sh <version>
Source1:        jquery_%{version}_node_modules.tar.gz

# disable gzip-js during build
Patch1:         %{name}-disable-gzip-js.patch


BuildRequires:  web-assets-devel
BuildRequires:  nodejs-packaging
BuildRequires:  nodejs

Provides:       jquery = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}%{ver_x} = %{version}-%{release}
Provides:       %{name}%{ver_x}-static = %{version}-%{release}

Requires:       web-assets-filesystem

# Bundles sizzle (https://github.com/jquery/sizzle/) in node_modules/sizzle
# Get version from package.json
Provides:       bundled(sizzle) = 2.3.5
Provides:       bundled(js-sizzle) = 2.3.5


%description
jQuery is a fast, small, and feature-rich JavaScript library. It makes things
like HTML document traversal and manipulation, event handling, animation, and
Ajax much simpler with an easy-to-use API that works across a multitude of
browsers. With a combination of versatility and extensibility, jQuery has
changed the way that millions of people write JavaScript.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -n jquery-%{version} -p1

#remove precompiled stuff
rm -rf dist/*

# Install the cached node modules
tar xf %{SOURCE1}


%build
./node_modules/grunt-cli/bin/grunt -v 'build:*:*' uglify


%check
./node_modules/grunt-cli/bin/grunt -v 'build:*:*' test:prepare test:fast


%install
%global installdir %{buildroot}%{_jsdir}/jquery

mkdir -p %{installdir}/%{version}
cp -p dist/* %{installdir}/%{version}

mkdir -p %{buildroot}%{_webassetdir}
ln -s ../javascript/jquery %{buildroot}%{_webassetdir}/jquery

ln -s %{version} %{installdir}/latest
ln -s %{version} %{installdir}/%{ver_x}
ln -s %{version} %{installdir}/%{ver_x}.%{ver_y}


%files
%{_jsdir}/jquery
%{_webassetdir}/jquery
%doc AUTHORS.txt CONTRIBUTING.md LICENSE.txt README.md


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.7.1-8
- Import
