%global source0_hash 66247b5449db64ebb93ae2ec4af4764b87d1ae8a7463c7c68893ac13fa8d4da2

%global gem_name rack-accept

Summary: HTTP Accept* for Ruby/Rack
Name: rubygem-%{gem_name}
Version: 0.4.5
Release: 24%{?dist}
License: MIT
URL: https://github.com/mjackson/rack-accept
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/mjackson/rack-accept/pull/23
Patch0:  rack-accept-pr23-rack3.patch
BuildRequires: rubygems-devel
BuildRequires: rubygem(rack)
BuildRequires: rubygem(test-unit)
BuildArch: noarch

%description
HTTP Accept, Accept-Charset, Accept-Encoding, and Accept-Language for
Ruby/Rack

%package doc
Summary: Documentation for %{gem_name}
Requires: %{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{gem_name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build ./%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ruby -Ilib -r ./test/helper -e "Dir.glob './test/**/*_test.rb', &method(:require)"
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/CHANGES
%doc %{gem_instdir}/README.md
%{gem_instdir}/test
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_docdir}

%changelog
%autochangelog
