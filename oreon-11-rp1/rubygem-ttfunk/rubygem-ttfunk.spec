%global source0_hash 2370ba484b1891c70bdcafd3448cfd82a32dd794802d81d720a64c15d3ef2a96

%global gem_name ttfunk

Summary: Font Metrics Parser for Prawn
Name: rubygem-%{gem_name}
Version: 1.7.0
Release: 14%{?dist}
# Automatically converted from old format: GPLv2 or GPLv3 or Ruby - review is highly recommended.
License: GPL-2.0-only OR GPL-3.0-only OR Ruby
URL: https://github.com/prawnpdf/ttfunk
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# Test suite is not packaged with the gem, you may check out it like so:
# git clone --no-checkout https://github.com/prawnpdf/ttfunk
# cd ttfunk && git archive -v -o ttfunk-1.7.0-spec.txz 1.7.0 spec
Source1: %{gem_name}-%{version}-spec.txz
# Reduired by: lib/ttfunk/table/cff/dict.rb
Requires: rubygem(bigdecimal)
BuildRequires: ruby
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygems
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(bigdecimal)
BuildArch: noarch

%description
TTFunk is a TrueType font parser written in pure ruby.

%package doc
BuildArch:  noarch
Requires:   %{name} = %{version}-%{release}
Summary:    Documentation for rubygem-%{gem_name}

%description doc
This package contains documentation for rubygem-%{gem_name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install
rm -rf ./%{gem_dir}/gems/%{gem_name}-%{version}/.yardoc

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec .

rspec spec
popd

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%license %{gem_instdir}/{COPYING,GPLv2,GPLv3,LICENSE}
%dir %{gem_instdir}
%{gem_instdir}/lib
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%{gem_spec}

%files doc
%doc %{gem_instdir}/{README.md,CHANGELOG.md}
%doc %{gem_docdir}

%changelog
%autochangelog
