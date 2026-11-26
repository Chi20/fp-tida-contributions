# Foundation Protocol inputs to FG-TIDA

## Propose a new work item

Follow the [FG-TIDA contribution guide](https://fg-tida.github.io/.github/#new).

## Contribute to an existing work item

Contributions to an adopted Working Group work item follow the
[existing-work-item procedure](https://fg-tida.github.io/.github/#existing).
Anything contributed is offered as input to the Working Group's work and may be
incorporated into its deliverables. Participation follows the ITU-T and FG-TIDA
participation, conduct, and IPR rules.

---

| Field | Value |
| --- | --- |
| Title | Versioned approval and authority provenance: Foundation Protocol reference inputs |
| Identifier | FP-TIDA-INPUTS |
| Contributor | Zhiyuan Ji (Chi20), individual capacity |
| Version | 0.1, 26 November 2026 |
| Intended discussion | Theme #16 / UC-4; PR #15 D2; proposed WG2 fixtures |
| Status | Individual informative contribution for review; not an adopted work item |
| DataTracker record | Not yet registered; routing enquiry pending |

Two separately reviewable contributions are provided:

1. [**Deferred-action checkpoint source packet**](src/doc/contributions/checkpoint-source-v0.1.rst)
   and its [JSON companion](src/doc/contributions/checkpoint-vectors-v0.1.json).
   Six hypothetical cases distinguish current approval, stale approval, reapproval,
   revocation, unavailable status, and acknowledgement without an observed effect.
2. [**Authority provenance mapping**](src/doc/contributions/d2-mapping-v0.1.rst).
   A separate informative input to D2 of PR #15, using an explicitly assumed PRC
   civil-law agency regime for three hypothetical cases and a bounded inspection
   of the FP paper and pinned code. No D2 conformance finding is claimed.

[Scope and proposed review sequence](src/doc/contributions/scope-and-routing.rst)
explains the interfaces with Themes #59/#60. Source review is requested before
freezing the fixture or undertaking an adapter evaluation. No FP runtime results
or human-participant study are reported. These inputs do not speak on behalf of
the Foundation Protocol authors, another contributor, or ITU.

## Build

The source layout and Furo styling derive from
[FG-TIDA/spec-template](https://github.com/FG-TIDA/spec-template/tree/f739b7d2461ecf963248f004f058f73e4fded26d).
The template's MIT notice is preserved. The configuration uses an individual
contribution title rather than an ITU publication cover.

```sh
python -m pip install -r requirements.txt
python -m sphinx -W --keep-going -b html src/doc target/html
```

Public discussion should cite a full commit SHA. A repository link or issue
comment alone does not register a contribution in the DataTracker.
