%global source0_hash 389e57e143b19082c9ba8ede4849f3d5ead5c0f3908e4ee9e56849215995e724
%bcond check 0
%bcond saml2 0
Name:       matrix-synapse
Version:    1.161.0
Release:        1%{?dist}
Summary:        A Matrix reference homeserver written in Python using Twisted
License:    AGPL-3.0-or-later
URL:        https://github.com/element-hq/synapse
%global upstream_tag v%{lua:return(rpm.expand("%{version}"):gsub("~",""))}
%global archive_tag %{lua:return(rpm.expand("%{version}"):gsub("~",""))}
Source0:        https://github.com/element-hq/synapse/archive/v%{version}/synapse-%{version}.tar.gz
Source1:    synapse.sysconfig
Source2:    synapse.service
Source3:    matrix-synapse.sysusers
Patch1:     0001-pyo3-Disable-abi3-feature.patch
Patch2:     0002-Build-RustExtension-with-debug-symbols.patch
Patch3:     0003-Remove-icu_segmenter.patch
ExclusiveArch:  %{rust_arches}
Recommends:     %{name}+postgres
Recommends:     %{name}+systemd
Recommends:     %{name}+user-search
%if %{with saml2}
%endif
%if %{without saml2}
Obsoletes:      %{name}+saml2 < 1.136.0-2
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(maturin) < 2.0
BuildRequires:  python3dist(maturin) >= 1.0
Requires:       python3-matrix-synapse = %{version}-%{release}
# /oreon:deps
%package -n       python3-matrix-synapse+matrix-synapse-ldap3
Summary:        Metapackage for python3-matrix-synapse matrix-synapse-ldap3 extras
Requires:       python3-matrix-synapse = %{version}-%{release}
Requires:       python3dist(matrix-synapse-ldap3) >= 0.1
Provides:       python3dist(matrix-synapse[matrix-synapse-ldap3]) = %{version}-%{release}

%description -n python3-matrix-synapse+matrix-synapse-ldap3
Metapackage for python3-matrix-synapse matrix-synapse-ldap3 extras.

%package -n       python3-matrix-synapse+postgres
Summary:        Metapackage for python3-matrix-synapse postgres extras
Requires:       python3-matrix-synapse = %{version}-%{release}
Requires:       python3dist(psycopg2) >= 2.8
Requires:       python3dist(psycopg2cffi) >= 2.8
Requires:       python3dist(psycopg2cffi-compat) == 1.1
Provides:       python3dist(matrix-synapse[postgres]) = %{version}-%{release}

%description -n python3-matrix-synapse+postgres
Metapackage for python3-matrix-synapse postgres extras.

%package -n       python3-matrix-synapse+saml2
Summary:        Metapackage for python3-matrix-synapse saml2 extras
Requires:       python3-matrix-synapse = %{version}-%{release}
Requires:       python3dist(pysaml2) >= 4.5.0
Requires:       python3dist(defusedxml) >= 0.7.1
Requires:       python3dist(pytz) >= 2018.3
Provides:       python3dist(matrix-synapse[saml2]) = %{version}-%{release}

%description -n python3-matrix-synapse+saml2
Metapackage for python3-matrix-synapse saml2 extras.

%package -n       python3-matrix-synapse+oidc
Summary:        Metapackage for python3-matrix-synapse oidc extras
Requires:       python3-matrix-synapse = %{version}-%{release}
Requires:       python3dist(authlib) >= 0.15.1
Provides:       python3dist(matrix-synapse[oidc]) = %{version}-%{release}

%description -n python3-matrix-synapse+oidc
Metapackage for python3-matrix-synapse oidc extras.

%package -n       python3-matrix-synapse+url-preview
Summary:        Metapackage for python3-matrix-synapse url-preview extras
Requires:       python3-matrix-synapse = %{version}-%{release}
Requires:       python3dist(lxml) >= 4.6.3
Provides:       python3dist(matrix-synapse[url-preview]) = %{version}-%{release}

%description -n python3-matrix-synapse+url-preview
Metapackage for python3-matrix-synapse url-preview extras.

%package -n       python3-matrix-synapse+sentry
Summary:        Metapackage for python3-matrix-synapse sentry extras
Requires:       python3-matrix-synapse = %{version}-%{release}
Requires:       python3dist(sentry-sdk) >= 0.7.2
Provides:       python3dist(matrix-synapse[sentry]) = %{version}-%{release}

%description -n python3-matrix-synapse+sentry
Metapackage for python3-matrix-synapse sentry extras.

%package -n       python3-matrix-synapse+opentracing
Summary:        Metapackage for python3-matrix-synapse opentracing extras
Requires:       python3-matrix-synapse = %{version}-%{release}
Requires:       python3dist(jaeger-client) >= 4.2.0
Requires:       python3dist(opentracing) >= 2.2.0
Requires:       python3dist(thrift) >= 0.10
Requires:       python3dist(tornado) >= 6.0
Provides:       python3dist(matrix-synapse[opentracing]) = %{version}-%{release}

%description -n python3-matrix-synapse+opentracing
Metapackage for python3-matrix-synapse opentracing extras.

%package -n       python3-matrix-synapse+jwt
Summary:        Metapackage for python3-matrix-synapse jwt extras
Requires:       python3-matrix-synapse = %{version}-%{release}
Provides:       python3dist(matrix-synapse[jwt]) = %{version}-%{release}

%description -n python3-matrix-synapse+jwt
Metapackage for python3-matrix-synapse jwt extras.

%package -n       python3-matrix-synapse+redis
Summary:        Metapackage for python3-matrix-synapse redis extras
Requires:       python3-matrix-synapse = %{version}-%{release}
Requires:       python3dist(txredisapi) >= 1.4.7
Requires:       python3dist(hiredis) >= 0.3
Provides:       python3dist(matrix-synapse[redis]) = %{version}-%{release}

%description -n python3-matrix-synapse+redis
Metapackage for python3-matrix-synapse redis extras.

%package -n       python3-matrix-synapse+cache-memory
Summary:        Metapackage for python3-matrix-synapse cache-memory extras
Requires:       python3-matrix-synapse = %{version}-%{release}
Requires:       python3dist(pympler) >= 1.0
Provides:       python3dist(matrix-synapse[cache-memory]) = %{version}-%{release}

%description -n python3-matrix-synapse+cache-memory
Metapackage for python3-matrix-synapse cache-memory extras.

%package -n       python3-matrix-synapse+test
Summary:        Metapackage for python3-matrix-synapse test extras
Requires:       python3-matrix-synapse = %{version}-%{release}
Requires:       python3dist(parameterized) >= 0.9.0
Requires:       python3dist(idna) >= 3.3
Provides:       python3dist(matrix-synapse[test]) = %{version}-%{release}

%description -n python3-matrix-synapse+test
Metapackage for python3-matrix-synapse test extras.

%package -n       python3-matrix-synapse+all
Summary:        Metapackage for python3-matrix-synapse all extras
Requires:       python3-matrix-synapse = %{version}-%{release}
Requires:       python3dist(matrix-synapse-ldap3) >= 0.1
Requires:       python3dist(psycopg2) >= 2.8
Requires:       python3dist(psycopg2cffi) >= 2.8
Requires:       python3dist(psycopg2cffi-compat) == 1.1
Requires:       python3dist(pysaml2) >= 4.5.0
Requires:       python3dist(authlib) >= 0.15.1
Requires:       python3dist(lxml) >= 4.6.3
Requires:       python3dist(sentry-sdk) >= 0.7.2
Requires:       python3dist(jaeger-client) >= 4.2.0
Requires:       python3dist(opentracing) >= 2.2.0
Requires:       python3dist(txredisapi) >= 1.4.7
Requires:       python3dist(hiredis) >= 0.3
Requires:       python3dist(pympler) >= 1.0
Requires:       python3dist(defusedxml) >= 0.7.1
Requires:       python3dist(pytz) >= 2018.3
Requires:       python3dist(thrift) >= 0.10
Requires:       python3dist(tornado) >= 6.0
Provides:       python3dist(matrix-synapse[all]) = %{version}-%{release}

%description -n python3-matrix-synapse+all
Metapackage for python3-matrix-synapse all extras.

%description
Matrix is an ambitious new ecosystem for open federated Instant Messaging and
VoIP. Synapse is a reference "homeserver" implementation of Matrix from the
core development team at matrix.org, written in Python/Twisted. It is intended
to showcase the concept of Matrix and let folks see the spec in the context of
a coded base and let you run your own homeserver and generally help bootstrap
the ecosystem.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n synapse-%{archive_tag}

# We don't support the built-in client so remove all the bundled JS.
rm -rf synapse/static

# We cannot respect upper bounds on the versions of Python build dependencies.
echo "$(tomcli get pyproject.toml build-system.requires -F json |
  jq '.[] |= sub("(,<=.*).*"; "") | .[]' -r)" |
  xargs -r -x tomcli set pyproject.toml lists str build-system.requires

%build

%pyproject_wheel
%install
%pyproject_install
%py3_shebang_fix %{buildroot}%{python3_sitearch}/synapse/_scripts
install -p -D -T -m 0644 contrib/systemd/log_config.yaml %{buildroot}%{_sysconfdir}/synapse/log_config.yaml
install -p -D -T -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/synapse
install -p -D -T -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/synapse.service
install -p -d -m 755 %{buildroot}%{_sharedstatedir}/synapse
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf
%oreon_autofiles main
%if %{with check}
%check

set -o pipefail
PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib}:$PWD trial-3 %{!?fc41:%_smp_mflags} tests | tee trial.stdout
WHITELIST="Requires hiredis
Requires jaeger_client
Requires Postgres
Test only applies when postgres is used as the database
not supported
not supported yet
Synapse does not correctly handle this case
\`BaseFederationServlet\` does not support cancellation yet.
Once we remove ops from the Sliding Sync response, this test should pass
Test is not possible because when everyone leaves the room, the server is \`no_longer_in_room\` and we don't have any \`current_state_events\` to query"
REASONS=$(cat trial.stdout | sed -n '/^\[SKIPPED\]$/{n;p;}')
SKIPPED=$(comm -23 <(echo "$REASONS" | sort | uniq) <(echo "$WHITELIST" | sort | uniq))
if [ ! -z "$SKIPPED" ]; then
  echo -e "Failing, because tests were skipped:\n$SKIPPED"
  exit 1
fi
%endif
%post

%systemd_post synapse.service
%preun

%systemd_preun synapse.service
%postun

%systemd_postun_with_restart synapse.service
%files

%changelog

%autochangelog
