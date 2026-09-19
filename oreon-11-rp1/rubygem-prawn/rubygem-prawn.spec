%global source0_hash 82062744f7126c2d77501da253a154271790254dfa8c309b8e52e79bc5de2abd

%global gem_name prawn

Summary: A fast and nimble PDF generator for Ruby
Name: rubygem-%{gem_name}
Version: 2.4.0
Release: 15%{?dist}
# afm files are licensed by APAFML, the rest of package is GPLv2 or GPLv3 or Ruby
# Automatically converted from old format: (GPLv2 or GPLv3 or Ruby) and APAFML - review is highly recommended.
License: ( GPL-2.0-only OR GPL-3.0-only OR Ruby ) AND APAFML
URL: http://prawnpdf.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Not all of data is shipped, but it's needed for the test suite.
# You may check out it like so:
# git clone --no-checkout https://github.com/prawnpdf/prawn.git
# cd prawn && git archive -v -o prawn-2.4.0-data.txz 2.4.0 data
Source1: %{gem_name}-%{version}-data.txz
BuildRequires: ruby
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: rubygem(matrix)
BuildRequires: rubygem(rspec) >= 3.0
BuildRequires: rubygem(ttfunk) >= 1.7
BuildRequires: rubygem(pdf-reader) >= 1.4.0
BuildRequires: rubygem(pdf-inspector) >= 1.2.1
BuildRequires: rubygem(pdf-core) >= 0.9.0
BuildArch: noarch

%description
Prawn is a pure Ruby PDF generation library that provides a lot of great
functionality while trying to remain simple and reasonably performant.
Here are some of the important features we provide:

- Vector drawing support, including lines, polygons, curves, ellipses, etc.
- Extensive text rendering support, including flowing text and limited inline
  formatting options.
- Support for both PDF builtin fonts as well as embedded TrueType fonts
- A variety of low level tools for basic layout needs, including a simple
  grid system
- PNG and JPG image embedding, with flexible scaling options
- Reporting tools for rendering complex data tables, with pagination support
- Security features including encryption and password protection
- Tools for rendering repeatable content (i.e headers, footers, and page
  numbers)
- Comprehensive internationalization features, including full support for UTF-8
  based fonts, right-to-left text rendering, fallback font support,
  and extension points for customizable text wrapping.
- Support for PDF outlines for document navigation
- Low level PDF features, allowing users to create custom extensions
  by dropping down all the way to the PDF object tree layer.
  (Mostly useful to those with knowledge of the PDF specification)
- Lots of other stuff!

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

# matrix is bundled gem since Ruby 3.1.
# https://github.com/prawnpdf/prawn/commit/3658d5125c3b20eb11484c3b039ca6b89dc7d1b7
%gemspec_add_dep -g matrix '~> 0.4'

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rm -rf data
ln -s %{_builddir}/data .

sed -i "/^require 'bundler'/d" ./spec/spec_helper.rb
sed -i "/^Bundler.setup/d" ./spec/spec_helper.rb

# manual_builder dependency is not in Fedora yet
mv spec/prawn_manual_spec.rb{,.disable}

# There are missing font and image files required by test suite.
# These are not bundled in the gem therefore some failures occur.
rspec spec
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/{LICENSE,COPYING,GPLv2,GPLv3}
%exclude %{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/data/fonts/*.afm
%exclude %{gem_instdir}/.yardopts

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%doc %{gem_instdir}/manual
%doc %{gem_instdir}/data/fonts/MustRead.html

%changelog
%autochangelog
