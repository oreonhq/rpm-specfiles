%global source0_hash 0a8512ecf6a8fe14928707f7d2766680c955b3a2224de198c1e25c837cd36f82

# Generated from color-1.4.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name color

Name: rubygem-%{gem_name}
Version: 1.8
Release: 21%{?dist}
Summary: Color management with Ruby
License: MIT
URL: https://github.com/halostatue/color
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fix compatibility with minitest6
Patch0:  color-1.8-minitest6.patch
# Remove frozen string warnings from ruby 3.4
Patch1:  color-1.8-frozen-string-warnings.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
Color is a Ruby library to provide basic RGB, CMYK, HSL, and other colourspace
manipulation support to applications that require it. It also provides 152
named RGB colours (184 with spelling variations) that are commonly supported
in HTML, SVG, and X11 applications. A technique for generating monochromatic
contrasting palettes is also included.

The Color library performs purely mathematical manipulation of the colours
based on colour theory without reference to colour profiles (such as sRGB or
Adobe RGB). For most purposes, when working with RGB and HSL colour spaces,
this won't matter. Absolute colour spaces (like CIE L*a*b* and XYZ) and cannot
be reliably converted to relative colour spaces (like RGB) without colour
profiles.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T
%gem_install -n %{SOURCE0}

pushd .%{gem_instdir}
%patch -P0 -p1
%patch -P1 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ruby -Ilib:test -e 'Dir.glob "./test/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/Licence.rdoc
%exclude %{gem_instdir}/.*
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Code-of-Conduct.rdoc
%doc %{gem_instdir}/Contributing.rdoc
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/Manifest.txt
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
%autochangelog
