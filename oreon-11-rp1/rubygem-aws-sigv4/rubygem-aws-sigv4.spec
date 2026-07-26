%global source0_hash 746efa6929bf16ec88b2768f04c53841c987dd28137c864366c6d7d985ff183c

%global gem_name aws-sigv4

Name:           rubygem-%{gem_name}
Version:        1.0.2
Release:        21%{?dist}
Summary:        AWS Signature Version 4 library

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://github.com/aws/aws-sdk-ruby
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone http://github.com/aws/aws-sdk-ruby aws-sdk-ruby; cd aws-sdk-ruby
# id=d6b12f0853633f00e6be5dcc9dbfda9d8676f39a
# git checkout $id
# cp -vp LICENSE.txt NOTICE.txt gems/aws-sigv4/
# (cd gems/aws-sigv4; tar -czf ../../rubygem-aws-sigv4-1.0.2-repo.tgz spec/ *.txt)
Source1:        %{name}-%{version}-repo.tgz
# https://github.com/aws/aws-sdk-ruby/pull/2179
# https://github.com/aws/aws-sdk-ruby/commit/9b37df5f8c656c9aaca3a8315b4afc685623e42c
# ruby3.2 removes File.exists?
Patch0:         %{name}-pr2179-ruby32-file_exists-removal.patch

BuildArch:      noarch
BuildRequires:  rubygems-devel
BuildRequires:  rubygem(rspec)
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       ruby(rubygems)
Provides:       rubygem(%{gem_name}) = %{version}-%{release}
%endif

%description
Amazon Web Services Signature Version 4 signing library. Generates sigv4
signature for HTTP requests.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n %{gem_name}-%{version}
tar -xzf %{SOURCE1}
%patch -P0 -p3

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
cp -pr spec/ ./%{gem_instdir}
pushd ./%{gem_instdir}
rspec -Ilib spec
rm -rf spec
popd

%files
%license LICENSE.txt NOTICE.txt
%dir %{gem_instdir}/
%{gem_libdir}/
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}/

%changelog
%autochangelog
