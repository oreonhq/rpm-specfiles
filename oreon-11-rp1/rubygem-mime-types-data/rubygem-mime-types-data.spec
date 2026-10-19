%global source0_hash e90f027e54346bbbf7bd993a97e9cb7270cd4fe41c535ef84bf5d1aefe1e7ede
%global gem_name mime-types-data
Name: rubygem-%{gem_name}
Version: 3.2023.0218.1
Release:        7%{?dist}
Summary:        A registry for information about MIME media type definitions
License: MIT
URL: https://github.com/mime-types/mime-types-data/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
mime-types-data provides a registry for information about MIME media type
definitions. It can be used with the Ruby mime-types library or other software
to determine defined filename extensions for MIME types, or to use filename
extensions to look up the likely MIME type definitions.

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
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-mime-types-data-doc -f %{oreon_filedir}/rubygem-mime-types-data-doc.list

%changelog

%autochangelog
