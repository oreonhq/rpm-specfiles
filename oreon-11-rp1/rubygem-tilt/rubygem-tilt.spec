%global source2_hash f9ff4b0e875882f336905bc607b0bcdb91bcb9266780170d621bbc7b24f0d778
%global source0_hash e76f850e611128a87992bb13ba74807624a9b8ec748e2c2ea7139580f67ab22e
%global gem_name tilt
%bcond_with bootstrap
Name: rubygem-%{gem_name}
Version: 2.2.0
Release:        1%{?dist}
Summary:        Generic interface to multiple Ruby template engines
License: MIT
URL: https://github.com/jeremyevans/tilt
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source2: https://github.com/jeremyevans/tilt/archive/refs/tags/v2.2.0.tar.gz
%if %{without bootstrap}
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(RedCloth)
BuildRequires:  rubygem(asciidoctor)
BuildRequires:  rubygem(builder)
BuildRequires:  rubygem(creole)
BuildRequires:  rubygem(erubi)
BuildRequires:  rubygem(kramdown)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(minitest-mock)
BuildRequires:  rubygem(nokogiri)
BuildRequires:  rubygem(pdf-reader)
BuildRequires:  rubygem(prawn)
BuildRequires:  rubygem(rdiscount)
BuildRequires:  rubygem(redcarpet)
BuildRequires:  rubygem(sassc)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Generic interface to multiple Ruby template engines.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version} -b 2
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
sed -i -e 's|/usr/bin/env ruby|/usr/bin/ruby|' %{buildroot}%{gem_instdir}/bin/tilt
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{without bootstrap}
%check

pushd .%{gem_instdir}
cp -a %{_builddir}/test test
LANG=C.UTF-8 ruby -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-tilt-doc -f %{oreon_filedir}/rubygem-tilt-doc.list

%changelog

%autochangelog
