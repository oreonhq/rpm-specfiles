%global source0_hash 97cd2fe153413df0f13f2b3bafe00c677045fdaa90f4d96d76e7e269baf296bb

%global gem_name sinatra-cross_origin

Name:           rubygem-%{gem_name}
Version:        0.4.0
Release:        17%{?dist}
Summary:        Cross Origin Resource Sharing helper for Sinatra

License:        MIT
URL:            http://github.com/britg/sinatra-cross_origin
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildArch:      noarch
BuildRequires:  rubygems-devel
BuildRequires:  rubygem(rack-test)
BuildRequires:  rubygem(sinatra)
BuildRequires:  rubygem(test-unit)

%description
Cross Origin Resource Sharing helper for Sinatra.

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

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ruby -Ilib:test -e 'Dir.glob "./test/test_all.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}/
%license %{gem_instdir}/LICENSE
%{gem_instdir}/VERSION
%{gem_libdir}/
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/test/
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec

%changelog
%autochangelog
