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
BuildRequires:  nodejs, /usr/bin/node

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
%autosetup -n jquery-%{version} -v -p1

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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.7.1-8
- Prepare for Oreon 11 (RP1)
