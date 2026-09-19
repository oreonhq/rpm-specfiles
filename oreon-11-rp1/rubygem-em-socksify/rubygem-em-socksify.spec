%global source0_hash 2a9feb13e65efc89434008e99dda9d80e11f9aa1a294dda60a2c400134896b89

%global gem_name em-socksify

Name: rubygem-%{gem_name}
Version: 0.3.0
Release: 33%{?dist}
Summary: Transparent proxy support for any EventMachine protocol
License: MIT
URL: https://github.com/igrigorik/em-socksify
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: MIT-LICENSE
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(base64)
BuildArch: noarch
%if 0%{?fc19} || 0%{?fc20}
Requires: ruby(release)
Requires: rubygems
Requires: rubygem(eventmachine) >= 1.0.0.beta.4
Provides: rubygem(%{gem_name}) = %{version}
%endif

%description
Transparent proxy support for any EventMachine protocol

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
%gemspec_add_dep -g base64 -s %{gem_name}.gemspec ">= 0.2.0"

%build
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
cp -p %{SOURCE1} %{buildroot}/%{gem_instdir}/

#Spec suite only includes 2 tests that require external connections,
#commented out since this isn't possible within mock
#%%check
#pushd ./%%{gem_instdir}
#rspec -Ilib spec
#popd

%files
%dir %{gem_instdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.gitignore
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE
%{gem_libdir}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/em-socksify.gemspec

%changelog
%autochangelog
