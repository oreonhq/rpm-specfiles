%global source0_hash 336d46e39e003f77bf973337a958af6a68300b941c85cb22288872dc2b36addb

%global gem_name prawn-table

Name: rubygem-%{gem_name}
Version: 0.2.2
Release: 24%{?dist}
Summary: Provides tables for PrawnPDF
# Automatically converted from old format: Ruby or GPLv2 or GPLv3 - review is highly recommended.
License: Ruby OR GPL-2.0-only OR GPL-3.0-only
URL: https://github.com/prawnpdf/prawn-table
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygem(prawn) >= 1.3.0
# data/images/prawn.png is required by test suite.
BuildRequires: rubygem-prawn-doc
BuildRequires: rubygem(pdf-inspector) => 1.1.0
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(pdf-reader) => 1.2
BuildArch: noarch

%description
Prawn::Table provides tables for the Prawn PDF toolkit.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
sed -i '/^require "bundler"/d' ./spec/spec_helper.rb
sed -i '/^Bundler.setup/d' ./spec/spec_helper.rb
# Don't run unresolved test cases.
# https://github.com/prawnpdf/prawn-table/blob/master/Rakefile#L15
# 4 failures expected due to image file not included in prawn gem
rspec spec -t ~unresolved \
  | tee /dev/stderr \
  | grep '222 examples, 4 failures'
# Currently disabled
# rspec2 spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/COPYING
%license %{gem_instdir}/GPLv2
%license %{gem_instdir}/GPLv3
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%{gem_instdir}/manual
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/prawn-table.gemspec
%{gem_instdir}/spec

%changelog
%autochangelog
