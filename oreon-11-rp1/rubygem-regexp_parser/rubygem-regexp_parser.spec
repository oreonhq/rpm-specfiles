%global source0_hash b8949b9ec53bb24bafdb262c6863174cdb72ee5a69e3508cfeb3da8414591ceb

# Generated from regexp_parser-1.7.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name regexp_parser

Name: rubygem-%{gem_name}
Version: 2.11.3
Release: 2%{?dist}
Summary: Scanner, lexer, parser for ruby's regular expressions
License: MIT
URL: https://github.com/ammar/regexp_parser
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/ammar/regexp_parser.git && cd regexp_parser
# git archive -v -o regexp_parser-2.11.3-specs.tar.gz v2.11.3 spec/
Source1: %{gem_name}-%{version}-specs.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.0.0
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(regexp_property_values)
BuildArch: noarch

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

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
( cd .%{gem_instdir}
ln -s %{_builddir}/spec spec

# We don't have 'leto' in Fedora.
sed -i '/leto/ s/^/#/' spec/spec_helper.rb
sed -i -r '/Leto/ s/Leto.deep_freeze\((.*)\)/\1/' spec/expression/to_s_spec.rb
sed -i -r '/Leto/i\    skip/' spec/expression/clone_spec.rb

rspec spec
)

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/regexp_parser.gemspec

%changelog
%autochangelog
