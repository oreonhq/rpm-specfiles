%global source0_hash 4f368b2f12b57ec979872d4bf4bd1a67e8648e0c81ab89801431d2fc89f4e0bb
%global gem_name pdf-core
Name: rubygem-%{gem_name}
Version: 0.9.0
Release:        1%{?dist}
Summary:        PDF::Core is used by Prawn to render PDF documents
License: GPL-2.0-only OR GPL-3.0-only OR Ruby 
URL: https://github.com/prawnpdf/pdf-core
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: %{gem_name}-%{version}-specs.tgz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(pdf-inspector)
BuildRequires:  rubygem(pdf-reader)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
PDF::Core is used by Prawn to render PDF documents.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version} -b1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
cp -r %{_builddir}/spec .
sed -i -e "s/require 'bundler'//" spec/spec_helper.rb
sed -i -e 's/Bundler.setup//' spec/spec_helper.rb
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-pdf-core-doc -f %{oreon_filedir}/rubygem-pdf-core-doc.list

%changelog

%autochangelog
