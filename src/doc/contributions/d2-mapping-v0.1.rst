Foundation Protocol records and authority provenance
=========================================================

:Contributor: Zhiyuan Ji (Chi20), individual capacity
:Version: 0.1, 26 November 2026
:Status: Separate informative mapping for review; no D2 conformance verdict
:Target: D2 of the Provenance of Authority charter, FG-TIDA/themes PR 15

Scope and reference boundary
----------------------------

This input responds to Pam Dixon's 14 October invitation. It maps selected FP
records to six distinctions: grant/capability, relationship/standing,
approval/origination, current grant status, receipt/authority, and regime/provenance.
It proposes no charter text and makes no statement on behalf of FP's authors.

The charter reference is commit
``54b5120ba45d347085bda2a8cd1992ead6e9ac8d``, scope elements 2 and 5, with
general clauses 0.1-0.6 in comment 5415722226. These general clauses do not
themselves supply the per-requirement decision tables. This mapping therefore
records bounded source findings and unresolved carriage questions, rather than
assigning a final ``can carry``, ``requires extension`` or ``cannot carry`` verdict.
The target is D2 of PR 15, not a similarly numbered deliverable in another charter.

The research reference is Bang Liu et al., arXiv:2605.23218v1, especially
A.4.1, A.4.3 and A.4.4. Implementation observations below refer only to commit
``2ea04c25363a495fde13166779c90b6a7c3c3780`` of
``FoundationAgents/foundation-protocol``. The paper and code are distinct sources;
this is a static inspection of named records, not a runtime evaluation or a
complete audit of every possible FP profile.

Assumed regime and attributed hypothetical facts
------------------------------------------------

Each case assumes **the law of the People's Republic of China, Civil Code,
Book One, Chapter VII, voluntary agency**, for an ordinary domestic commercial
mandate. The regime is selected solely to make these hypothetical cases explicit;
it is not asserted to govern FP deployments or use case 10.

Articles 161-165 address agency and written authorization. Articles 171-172
distinguish unauthorized action and circumstances of apparent authority;
article 173 addresses termination, including cancellation of the mandate.
These references identify relevant distinctions. They do not turn signature
verification or a protocol record into a legal determination.

The following facts and supplied determinations are authored by this
contribution's contributor solely as case stipulations. No external lawyer,
court, institution or FP author is represented as having made them.

P is a principal and O a distinct operator, each a legal person with the relevant
capacity. S is O's software instrument, not a civil-law person or the legal
grantee. Where G exists, P has expressly authorized O, in P's name, to place
one specified ordinary purchase order with T, within a stated amount, scope and
period. The case stipulates satisfied conferral and form requirements; the
instrument identity binding is an independent supplied fact. No cross-border,
employment-agency or onward-delegation issue is introduced.

Origination and act-time determinations have separate identities, authors and
effective times even when their values agree. The statements below are the
author's illustrative inputs, not conclusions drawn by an FP verifier. A real
mapping would replace them with attributed case evidence and the relevant
legal determination; this draft evaluates no real mandate and gives no legal advice.

Case M1: relationship and capability without an established grant
----------------------------------------------------------------------

**Regime:** PRC Civil Code voluntary agency, articles 161-165 and 171-172.

**Supplied facts:** at t0, S advertises an ordering capability and has an accepted
friend relationship. A relying party's search of the stipulated evidence set
contains no established G; this is an observation about that set, not a claim
that no grant exists anywhere. Origination and act-time standing are both
``not_established_from_supplied_evidence``. The existence of ratification or
apparent authority is not inferred from the software relationship.

**FP evidence:** ``FriendRequestPayload.sender_card`` in ``fp/message.py`` and
the documented ``FriendCheckPoint`` concern a peer relationship. The known-gaps
document distinguishes the initial card claim from externally validated identity.

**Mapping:** identify the card's declarant/observed sender separately from an
alleged grantor. A friend relation and capability claim do not themselves supply
G's author, legal grantee, conferred bounds or standing. A report of an unsuccessful
search needs its author, examined scope, period and as-of time. No dedicated
absence-assertion or legal-mandate construct is established by these selected
payload fields. This is a bounded finding, not proof that an external profile
could not add one.

Case M2: recorded approval with a separately supplied mandate
------------------------------------------------------------------

**Regime:** PRC Civil Code voluntary agency, articles 161-165.

**Supplied facts:** G was validly conferred at t0 and remains applicable at act
time t2 for the stipulated order. O operates S. H is a technical reviewer whose
assigned review scope is separately supplied. At t1 H approves one order state.
That response does not author or retrospectively establish G.

**FP evidence:** generic owner approval uses ``ApprovalRequestPayload`` and
``ApprovalResponsePayload``, with ``request_id`` and an approval action. The
contract subsystem also defines ``ContractApproval.approved_revision``,
``approved_terms_hash``, ``approved_at`` and ``approved_by``. This is an existing
revision/hash binding and should not be described as wholly absent from FP.

**Mapping:** retain the useful distinction between an approval of specified
contract terms and a generic pending-message response. Neither the field name
``approved_by`` nor a terms hash establishes the legal conferral from P to O.
The selected approval models have no dedicated fields stating G's legal regime,
its legally identified grantor/grantee, or the attributed origination and act-time
determinations. Additional carriage and interpretation rules would need to say
how those facts are expressed and joined to the approval. The technical
checkpoint packet independently proposes action/state binding for a controlled
tool; it does not report that all generic owner responses already enforce it.

Case M3: prior signed record after a supplied change of mandate
--------------------------------------------------------------------

**Regime:** PRC Civil Code voluntary agency, articles 171-173.

**Supplied facts:** G was validly conferred at t0; cancellation takes effect at
t1 before the attempted order t2. For this illustrative case, the attributed
act-time determination stipulates that G no longer authorizes this act, T knows
of the cancellation, and neither ratification nor apparent authority preserves
effect. These are explicit premises, not a general claim that every cancellation
has the same effect against every third party. The t0 conferral remains historical.

**FP evidence:** ``ContractReceipt`` records an acknowledgement tied to a
``snapshot_hash``; ``ArbiterAttestation`` identifies and signs a snapshot with
a prior-snapshot link. ``ContractSnapshot`` carries contract status and approval
history. Contract lifecycle role/status checks are implemented in
``fp/trade/authorize.py``.

**Mapping:** a historical signature or acknowledgement can remain valid while the
supplied mandate's act-time status changes. A contract status is not automatically
the status of the distinct P-to-O mandate. The selected models do not establish
a consultation result for that mandate, including record version/recency,
reachability and the provenance of the changed determination. An unreachable
mandate record yields no current finding; it is distinct from a supplied revoked
status. Any authority established after t2 must be represented as a later record,
not a rewrite of what the t2 observer could establish.

Carriage questions for D2 review
-------------------------------------

FP's signed envelopes and versioned contract records provide useful candidate
locations for attributable data. ``Message.metadata`` and payload dictionaries
can hold application data, but byte capacity alone does not define interoperable
authority semantics. An assessment profile needs to identify the carried fields,
producers, meanings and consumer rules before testing the D2 distinctions.

The proposed next mapping rows are: grant and person/instrument binding;
scope/period; regime and attributed determinations at both moments; search-scoped
absence; observed-source versus grantor role; later authority as a new record;
and act-time consultation result. For each, compare the candidate representation
against a specified D2 table revision once available. Missing information remains
explicit. No legal status is manufactured to fill a field.

This input does not change the facts of use case 10, does not assign personhood
to software, and does not report an FP conformance result. Review is requested on
the bounded mappings and on which table revision should govern a later assessment.

References
----------

* `Invitation <https://github.com/FG-TIDA/themes/pull/15#issuecomment-6180058259>`_
* `Charter at the assessed revision <https://github.com/FG-TIDA/themes/blob/54b5120ba45d347085bda2a8cd1992ead6e9ac8d/PROVENANCE-OF-AUTHORITY-CHARTER.md>`_
* `D2 general clauses <https://github.com/FG-TIDA/themes/pull/15#issuecomment-5415722226>`_
* `Paper v1 <https://arxiv.org/html/2605.23218v1>`_
* `FP approval payloads <https://github.com/FoundationAgents/foundation-protocol/blob/2ea04c25363a495fde13166779c90b6a7c3c3780/fp/message.py>`_
* `FP contract models <https://github.com/FoundationAgents/foundation-protocol/blob/2ea04c25363a495fde13166779c90b6a7c3c3780/fp/trade/models.py>`_
* `FP contract authorization <https://github.com/FoundationAgents/foundation-protocol/blob/2ea04c25363a495fde13166779c90b6a7c3c3780/fp/trade/authorize.py>`_
* `FP documented boundaries <https://github.com/FoundationAgents/foundation-protocol/blob/2ea04c25363a495fde13166779c90b6a7c3c3780/docs/security/known-gaps.md>`_
* `PRC Civil Code, official Chinese text, Chapter VII <https://www.cac.gov.cn/2020-06/01/c_1592561777268319.htm>`_
