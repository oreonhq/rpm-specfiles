%global source0_hash 4702644ac6d63ebbddff372a3cd4cd573513287e3524b5a5415f678970057a4b
%global gem_name rack-cors
Name:           rubygem-%{gem_name}
Version:        1.1.1
Release:        1%{?dist}
Summary:        Middleware for enabling Cross-Origin Resource Sharing in Rack apps
License:        MIT
URL:            https://github.com/cyu/rack-cors
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:         rack-cors-pr266-minitest-mocha-compatibility.patch
Patch1:         rack-cors-1.1.1-rack3-compat.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  rubygem(logger)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(mocha)
BuildRequires:  rubygem(rack-test)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Middleware that will make Rack-based apps CORS compatible.

Fork the project here: https://github.com/cyu/rack-cors.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}
%patch -P0 -p1
%patch -P1 -p1

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# ref: https://github.com/cyu/rack-cors/pull/286
%gemspec_add_dep -g logger -s %{gem_name}.gemspec

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ruby -rminitest/autorun -Ilib -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rack-cors-doc -f %{oreon_filedir}/rubygem-rack-cors-doc.list

%changelog

%autochangelog
