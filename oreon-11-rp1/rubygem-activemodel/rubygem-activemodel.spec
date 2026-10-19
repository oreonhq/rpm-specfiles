%global source1_hash 0419bf47f7357e6d3da85ff4ad797a3609dcf36ff44be496162ffbc901ff4232
%global source0_hash 406907245a1c6c04cdf2187cc4590fdc081d7a07392123d322125677022ea67c
%global gem_name activemodel
%bcond_with bootstrap
Name: rubygem-%{gem_name}
Version: 8.0.3
Release:        1%{?dist}
Summary:        A toolkit for building modeling frameworks (part of Rails)
License: MIT
URL: https://rubyonrails.org
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/rails/rails/archive/refs/tags/v8.0.3.tar.gz
%{!?with_bootstrap:BuildRequires: rubygem(railties) = %{version}}
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(activesupport)
BuildRequires:  rubygem(bcrypt)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A toolkit for building modeling frameworks like Active Record. Rich support
for attributes, callbacks, validations, serialization, internationalization,
and testing.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

( cd .%{gem_instdir}
cp -a %{builddir}/test .
mkdir ../tools
touch ../tools/test_common.rb
touch ../tools/strict_warnings.rb
%if %{with bootstrap}
mv ./test/cases/railtie_test.rb{,.disable}
%endif
ruby -Ilib:test -e "Dir.glob('./test/**/*_test.rb').sort.each {|t| require t}"
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-activemodel-doc -f %{oreon_filedir}/rubygem-activemodel-doc.list

%changelog

%autochangelog
