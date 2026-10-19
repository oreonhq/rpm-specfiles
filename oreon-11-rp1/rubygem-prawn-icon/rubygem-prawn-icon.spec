%global source0_hash b3c1d88823ae0648691ca6053e8c9a2863b306824a1ed71a4c38128f97203311
%global gem_name prawn-icon
Name: rubygem-%{gem_name}
Version: 3.1.0
Release:        1%{?dist}
Summary:        Provides icon fonts for PrawnPDF
License: Ruby OR GPL-2.0-only OR GPL-3.0-only
URL: https://github.com/jessedoyle/prawn-icon/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(pdf-inspector)
BuildRequires:  rubygem(prawn)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Prawn::Icon provides various icon fonts including
FontAwesome, Foundation Icons and GitHub Octicons
for use with the Prawn PDF toolkit.

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i "/require \"bundler\"/ s/^/#/" spec/spec_helper.rb
sed -i "/Bundler.setup/ s/^/#/" spec/spec_helper.rb
sed -i "/require 'simplecov'/ s/^/#/" spec/spec_helper.rb
sed -i "/SimpleCov.start/ s/^/#/" spec/spec_helper.rb
rspec -rprawn spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-prawn-icon-doc -f %{oreon_filedir}/rubygem-prawn-icon-doc.list

%changelog

%autochangelog
