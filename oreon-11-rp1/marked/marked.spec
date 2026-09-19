%global source0_hash f922aa64b2ca32fd1543d3af3b35705e4161e7f5abcd6ffbcad7b44f84fbdfd8

%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       marked
Version:    2.0.0
Release:    13%{?dist}
Summary:    A markdown parser for Node.js built for speed
License:    MIT
URL:        https://github.com/markedjs/%{name}
Source0:    https://github.com/markedjs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging
BuildRequires:  web-assets-devel
BuildRequires:  uglify-js

%if 0%{?enable_tests}
BuildRequires:  jasmine
BuildRequires:  npm
#BuildRequires:  npm(express)
BuildRequires:  npm(markdown)
BuildRequires:  npm(showdown)
# Not yet packaged for Fedora.
# BuildRequires:  npm(robotskirt)
%endif

Requires:       nodejs-marked = %{version}-%{release}

%global _description\
marked is a full-featured markdown compiler that can parse huge chunks of\
markdown without having to worry about caching the compiled output or\
blocking for an unnecessarily long time.\
\
marked is extremely fast and frequently outperforms similar markdown parsers.\
marked is very concise and still implements all markdown features, as well\
as GitHub Flavored Markdown features.\
\
marked more or less passes the official markdown test suite in its entirety.\
This is important because a surprising number of markdown compilers cannot\
pass more than a few tests.

%description
Install this for command line tool and man page.
%_description

# Note: the subpackages were the only way I could get upgrades
# from marked-0.3.2 or nodejs-marked-0.3.6 to work smoothly.

%package -n nodejs-marked
Summary:    A markdown parser for JavaScript built for speed
# For symlink in %%{nodejs_sitelib}/%%{name}/lib
Requires:       js-marked = %{version}-%{release}

%description -n nodejs-marked %_description

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

%if 0%{?enable_tests}
%check
# gfm_code_hr_list test is known to fail but the author has not yet arrived
# at a satisfactory solution: https://github.com/chjj/marked/pull/118

# def_blocks and double_link are also known to fail:
# https://github.com/chjj/marked/issues/136#issuecomment-15016714

%nodejs_symlink_deps --check
# /usr/bin/npm install robotskirt
#__nodejs ./test/
npm run test
%endif

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files -n nodejs-%{name}
%license LICENSE.md
%doc README.md docs
%{nodejs_sitelib}/%{name}

%files -n js-%{name}
%license LICENSE.md
%{_jsdir}/%{name}

%changelog
%autochangelog
