%global source0_hash 4ee5cb30341627a1d5d928e02353dd69e8c00e8a6301815762e253ce3a9e84af

%global gem_name stomp

Summary: Ruby client for the Stomp messaging protocol
Name: rubygem-%{gem_name}
Version: 1.4.10
Release: %autorelease
License: Apache-2.0
URL: https://github.com/stompgem/stomp
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/stompgem/stomp/pull/175
Patch0: https://salsa.debian.org/ruby-team/ruby-stomp/-/raw/5be6383a7a34a1d1891708d6aa8688cb4a6f89a5/debian/patches/fix-FTBFS-with-ruby-rspec-3.12.patch
BuildRequires: rubygems-devel 
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Ruby client for the Stomp messaging protocol

%package doc
Summary: Documentation for %{name}

Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}
%patch -P 0 -p1

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd %{buildroot}/%{gem_instdir}
rspec  -Ilib spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/catstomp
%{_bindir}/stompcat
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/stomp.gemspec
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTORS.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/spec
%doc %{gem_instdir}/notes
%doc %{gem_instdir}/examples
%doc %{gem_instdir}/test
%doc %{gem_instdir}/adhoc

%changelog
%autochangelog
