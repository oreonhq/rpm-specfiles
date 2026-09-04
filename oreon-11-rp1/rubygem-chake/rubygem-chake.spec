%global source0_hash 1b105e769ce0fd90108096db59b767691d69f67e5e9b28776f2b3b9cdd8a7c55

%global gem_name chake

Name: rubygem-%{gem_name}
Version: 0.21.2
Release: 14%{?dist}
Summary: Serverless configuration management tool for chef
License: MIT
URL: https://gitlab.com/terceiro/chake
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(asciidoctor)
BuildArch: noarch

%description
chake allows one to manage a number of hosts via SSH by combining chef (solo)
and rake. It doesn't require a chef server; all you need is a workstation from
where you can SSH into all your hosts. chake automates copying the
configuration management repository to the target host (including managing
encrypted files), running chef on them, and running arbitrary commands on the
hosts.

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
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

sed -f .%{gem_instdir}/man/readme2man.sed README.md > \
  .%{gem_instdir}/man/chake.adoc || \
  (rm -f .%{gem_instdir}/man/chake.adoc; false)
asciidoctor --backend manpage --out-file .%{gem_instdir}/man/chake.1 \
  .%{gem_instdir}/man/chake.adoc

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{gem_instdir}/man/chake.1 %{buildroot}%{_mandir}/man1

# Run the test suite
%check
pushd .%{gem_instdir}
rspec -Ilib spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/chake
%exclude %{gem_instdir}/coverage
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/bin
%exclude %{gem_instdir}/chake.spec.erb
%{gem_libdir}
%exclude %{gem_instdir}/man
%exclude %{gem_cache}
%exclude %{gem_instdir}/tags
%{gem_spec}
%doc %{_mandir}/man1/*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/ChangeLog.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/chake.gemspec
%{gem_instdir}/examples
%{gem_instdir}/spec

%changelog
%autochangelog
