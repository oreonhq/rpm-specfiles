%global source0_hash none

Name:           python-sentry-sdk
Version:        2.70.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        Python client for Sentry _https://sentry.io_

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://docs.sentry.io/platforms/python/
Source:         %{pypi_source sentry_sdk}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'sentry-sdk' generated automatically by pyp2spec.}

Patch0:         0001-Downstream-only-unpin-virtualenv.patch
Patch1:         0002-Add-django.contrib.admin-to-INSTALLED_APPS-to-fix-te.patch

%description %_description

%package -n     python3-sentry-sdk
Summary:        %{summary}

%description -n python3-sentry-sdk %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-sentry-sdk aiohttp,anthropic,arq,asyncio,asyncpg,beam,bottle,celery,celery-redbeat,chalice,clickhouse-driver,django,falcon,fastapi,flask,google-genai,grpcio,http2,httpx,huey,huggingface-hub,langchain,langgraph,launchdarkly,litellm,litestar,loguru,mcp,openai,openfeature,opentelemetry,opentelemetry-experimental,opentelemetry-otlp,pure-eval,pydantic-ai,pymongo,pyspark,quart,rq,sanic,sqlalchemy,starlette,starlite,statsig,tornado,unleash


%prep
%autosetup -p1 -n sentry_sdk-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x aiohttp,anthropic,arq,asyncio,asyncpg,beam,bottle,celery,celery-redbeat,chalice,clickhouse-driver,django,falcon,fastapi,flask,google-genai,grpcio,http2,httpx,huey,huggingface-hub,langchain,langgraph,launchdarkly,litellm,litestar,loguru,mcp,openai,openfeature,opentelemetry,opentelemetry-experimental,opentelemetry-otlp,pure-eval,pydantic-ai,pymongo,pyspark,quart,rq,sanic,sqlalchemy,starlette,starlite,statsig,tornado,unleash


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-sentry-sdk -f %{pyproject_files}

%changelog
%autochangelog
