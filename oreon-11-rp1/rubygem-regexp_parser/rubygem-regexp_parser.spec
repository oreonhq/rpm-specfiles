%global source1_hash c7322e78868c3a96dcc9786884ba656431d71b5c7bc4fecb3cbe7d60385e880e
%global source0_hash ca13f381a173b7a93450e53459075c9b76a10433caadcb2f1180f2c741fc55a4
%global gem_name regexp_parser
Name: rubygem-%{gem_name}
Version: 2.11.3
Release:        1%{?dist}
Summary:        Scanner, lexer, parser for ruby's regular expressions
License: MIT
URL: https://github.com/ammar/regexp_parser
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/ammar/regexp_parser/archive/refs/tags/v2.11.3.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(regexp_property_values)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A library for tokenizing, lexing, and parsing Ruby regular expressions.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version} -b 1
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
ln -s %{_builddir}/spec spec
sed -i '/leto/ s/^/#/' spec/spec_helper.rb
sed -i -r '/Leto/ s/Leto.deep_freeze\((.*)\)/\1/' spec/expression/to_s_spec.rb
sed -i -r '/Leto/i\    skip/' spec/expression/clone_spec.rb
rspec spec
)
%files -f %{oreon_filedir}/main.list
%files -n rubygem-regexp_parser-doc -f %{oreon_filedir}/rubygem-regexp_parser-doc.list

%changelog

%autochangelog
