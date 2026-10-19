%global source0_hash 9b452928c964b7c54c09aeb25ff045b5a722b387b16c9ce37cb1baec00062966
%global gem_name log4r
Name: rubygem-%{gem_name}
Version: 1.1.10
Release:        1%{?dist}
Summary:        Log4r, logging framework for ruby
License: LGPL-3.0-only
URL: https://github.com/colbygk/log4r
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: LICENSE
Source2: LICENSE.LGPLv3
Patch0: rubygem-log4r-1.1.10-Use-Psych.load_stream-instead-of-deprecated-Psych.lo.patch
Patch1: rubygem-log4r-1.1.10-First-parameter-of-assert-is-always-what-is-expected.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  rubygem(builder)
BuildRequires:  rubygem(rexml)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
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

gem build %{gem_name}.gemspec
%gem_install
install -m 644 %{SOURCE1} .%{gem_instdir}/LICENSE
install -m 644 %{SOURCE2} .%{gem_instdir}/LICENSE.LGPLv3
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
rm -rf %{buildroot}%{gem_instdir}/lib/log4r/rdoc
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}/tests
sed -i '/Configurator.load_xml_file "xml\/testconf.xml"/ s|xml/||' testxmlconf.rb
sed -i '/test_load[24]/a \
    omit' testxmlconf.rb
mkdir junk
for f in test*.rb; do
  LANG=C.UTF-8 ruby -I.:../lib $f
done
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-log4r-doc -f %{oreon_filedir}/rubygem-log4r-doc.list

%changelog

%autochangelog
