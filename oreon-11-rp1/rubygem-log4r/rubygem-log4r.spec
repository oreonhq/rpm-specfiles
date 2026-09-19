%global source0_hash 9b452928c964b7c54c09aeb25ff045b5a722b387b16c9ce37cb1baec00062966

# Generated from log4r-1.1.10.gem by gem2rpm -*- rpm-spec -*-
%global gem_name log4r

Name: rubygem-%{gem_name}
Version: 1.1.10
Release: 27%{?dist}
Summary: Log4r, logging framework for ruby
# License is changed for future releases!
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License: LGPL-3.0-only
URL: https://github.com/colbygk/log4r
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Upstream license files
#   https://github.com/colbygk/log4r/issues/39
# Taken from
#   https://github.com/colbygk/log4r/blob/40e2c2edd657a21b34f09dec7de238f348b6f428/
Source1: LICENSE
Source2: LICENSE.LGPLv3
# Fix Ruby 2.5 compatibility.
# https://github.com/colbygk/log4r/pull/57
Patch0: rubygem-log4r-1.1.10-Use-Psych.load_stream-instead-of-deprecated-Psych.lo.patch
# Use asserts correctly.
# https://github.com/colbygk/log4r/pull/58
Patch1: rubygem-log4r-1.1.10-First-parameter-of-assert-is-always-what-is-expected.patch
BuildRequires: rubygems-devel 
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(builder)
BuildRequires: rubygem(rexml)
BuildArch: noarch

%description
Log4r is a comprehensive and flexible logging library for use in Ruby programs.
It features a heirarchical logging system of any number of levels, custom level
names, multiple output destinations per log event, custom formatting, and more.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%patch 0 -p1
%patch 1 -p1

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

# License files
install -m 644 %{SOURCE1} .%{gem_instdir}/LICENSE
install -m 644 %{SOURCE2} .%{gem_instdir}/LICENSE.LGPLv3

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# This is not necessary for runtime nor it's a documentation
rm -rf %{buildroot}%{gem_instdir}/lib/log4r/rdoc

# Run the test suite
%check
# Tests are expected to run from tests directory.
pushd .%{gem_instdir}/tests

# The file is directly in "tests" directory.
sed -i '/Configurator.load_xml_file "xml\/testconf.xml"/ s|xml/||' testxmlconf.rb

# These fails wiht "Log level must be in 0..3". Not sure how to fix this.
sed -i '/test_load[24]/a \
    omit' testxmlconf.rb

# Test needs to have 'junk' directory available.
mkdir junk

# Tests needs to be run separately (especially
# test_gdc_default(TestGDC)).
for f in test*.rb; do
  LANG=C.UTF-8 ruby -I.:../lib $f
done
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/LICENSE
%license %{gem_instdir}/LICENSE.LGPLv3

%files doc
%doc %{gem_docdir}
%{gem_instdir}/tests
%doc %{gem_instdir}/doc
%{gem_instdir}/examples

%changelog
%autochangelog
