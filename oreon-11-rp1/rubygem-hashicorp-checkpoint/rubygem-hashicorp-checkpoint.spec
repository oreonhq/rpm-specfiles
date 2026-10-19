%global source0_hash 4daf74afd63c1701a6c817d87e4fc58f595037ccbc1d302bc45cdcd3f6e7d5fc
%global gem_name hashicorp-checkpoint
Name: rubygem-%{gem_name}
Version: 0.1.5
Release:        1%{?dist}
Summary:        Internal HashiCorp service to check version information
License: MPL-2.0
URL: http://www.hashicorp.com
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Internal HashiCorp service to check version information.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rubygem-hashicorp-checkpoint-doc -f %{oreon_filedir}/rubygem-hashicorp-checkpoint-doc.list

%changelog

%autochangelog
