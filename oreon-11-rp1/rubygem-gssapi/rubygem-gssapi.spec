%global source0_hash c51cf30842ee39bd93ce7fc33e20405ff8a04cda9dec6092071b61258284aee1
%global gem_name gssapi
Name: rubygem-%{gem_name}
Version: 1.3.1
Release:        1%{?dist}
Summary:        A FFI wrapper around the system GSSAPI library
License: MIT
URL: http://github.com/zenchild/gssapi
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
Requires: rubygem(ffi) >= 1.0.1
Requires: krb5-libs
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A FFI wrapper around the system GSSAPI library. Please make sure and read
the Yard docs or standard GSSAPI documentation if you have any questions.
There is also a class called GSSAPI::Simple that wraps many of the common
features used for GSSAPI.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}

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
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
rm -f %{buildroot}%{gem_instdir}/%{gem_name}.gemspec
rm %{buildroot}%{gem_instdir}/.gitignore
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rubygem-gssapi-doc -f %{oreon_filedir}/rubygem-gssapi-doc.list

%changelog

%autochangelog
