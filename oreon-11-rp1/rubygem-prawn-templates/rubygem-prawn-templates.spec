%global source0_hash 117aa03db570147cb86fcd7de4fd896994f702eada1d699848a9529a87cd31f1

%global gem_name prawn-templates

Name: rubygem-%{gem_name}
Version: 0.1.2
Release: 15%{?dist}
Summary: Prawn::Templates allows using PDFs as templates in Prawn
# Automatically converted from old format: Ruby or GPLv2 or GPLv3 - review is highly recommended.
License: Ruby OR GPL-2.0-only OR GPL-3.0-only
URL: https://github.com/prawnpdf/prawn-templates
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/prawnpdf/prawn-templates.git && cd prawn-templates
# git checkout 0.1.2
# tar -czf rubygem-prawn-templates-0.1.2-spec-data.tgz spec/ data/
Source1: %{name}-%{version}-spec-data.tgz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(prawn)
BuildRequires: rubygem-prawn-doc
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(pdf-reader)
BuildRequires: rubygem(pdf-inspector)
BuildArch: noarch

%description
Prawn::Templates allows using PDFs as templates in Prawn.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
mv %{_builddir}/{spec,data} .
%gemspec_remove_dep -g pdf-reader "~> 2.0"
%gemspec_add_dep -g pdf-reader ">= 2.0"

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
sed -i "/require 'bundler'/ s/^/#/" spec/spec_helper.rb
sed -i "/Bundler/ s/^/#/" spec/spec_helper.rb
rspec spec

%files
%dir %{gem_instdir}
%license %{gem_instdir}/COPYING
%license %{gem_instdir}/GPLv2
%license %{gem_instdir}/GPLv3
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/prawn-templates.gemspec

%changelog
%autochangelog
