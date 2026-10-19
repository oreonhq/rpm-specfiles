%global source0_hash 2c4755dfb5d6190e9ebb4407b23ac5a5c2c226be1449e6d3bdf625656352efd1
%global gem_name curb
Name: rubygem-%{gem_name}
Version: 1.0.5
Release:        1%{?dist}
Summary:        Ruby libcurl bindings
License: Ruby
URL: https://github.com/taf2/curb
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-curb-1.0.5-Use-TestServlet-url-instead-of-external-connectivity.patch
Patch1: rubygem-curb-1.0.5-fix-callback-function-read_data_handler.patch
# oreon:deps
BuildRequires:  /usr/bin/ss
BuildRequires:  gcc
BuildRequires:  libcurl-devel
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(webrick)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Curb (probably CUrl-RuBy or something) provides Ruby-language bindings for the
libcurl(3), a fully-featured client-side URL transfer library. cURL and
libcurl live at http://curl.haxx.se/.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%patch 0 -p1
%patch 1 -p1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
rm -rf %{buildroot}%{gem_instdir}/ext/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i '/omit/ s/^/#/' tests/tc_curl_multi.rb
ruby -I$(dirs +1)%{gem_extdir_mri} -e 'Dir.glob "./tests/tc_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-curb-doc -f %{oreon_filedir}/rubygem-curb-doc.list

%changelog

%autochangelog
