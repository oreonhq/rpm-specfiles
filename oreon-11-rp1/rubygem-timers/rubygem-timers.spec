%global source0_hash f45ca1b8ce6b26e29226c2144c512801a9019c3e781054d878c205cb0fd8500d
%global gem_name timers
Name: rubygem-%{gem_name}
Version: 4.0.1
Release:        1%{?dist}
Summary:        Pure Ruby one-shot and periodic timers
License: MIT
URL: https://github.com/celluloid/timers
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(hitimes)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Schedule procs to run after a certain time using any API that accepts a timeout

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
sed -i '/#!/d' %{buildroot}%{gem_instdir}/Rakefile
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i '/bundler/ s/^/#/' spec/spec_helper.rb
sed -i '/[Cc]overalls/ s/^/#/' spec/spec_helper.rb
sed -i '/ruby-prof/ s/^/#/' spec/performance_spec.rb
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-timers-doc -f %{oreon_filedir}/rubygem-timers-doc.list

%changelog

%autochangelog
